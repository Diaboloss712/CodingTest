import java.util.*;

class Solution {
    
    static class Node {
        int to;
        int cost;
        
        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }
    
    static final int INF = Integer.MAX_VALUE;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        List<List<Node>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for(int[] fare: fares) {
            int start = fare[0];
            int end = fare[1];
            int cost = fare[2];
            
            graph.get(start).add(new Node(end, cost));
            graph.get(end).add(new Node(start, cost));
        }
        
        int[] distS = dijkstra(n, s, graph);
        int[] distA = dijkstra(n, a, graph);
        int[] distB = dijkstra(n, b, graph);
        
        int answer = INF;
        
        for (int k = 1; k <= n; k++) {
            long total = (long)distS[k] + distA[k] + distB[k];
            answer = (int)Math.min(answer, total);
        }
        
        return answer;
    }
    
    private int[] dijkstra(int n, int start, List<List<Node>> graph) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>(
            Comparator.comparingInt(n1 -> n1.cost)
        );
        
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            
            if (current.cost > dist[current.to]) continue;
            
            for (Node next : graph.get(current.to)) {
                int newCost = current.cost + next.cost;
                
                if (newCost < dist[next.to]) {
                    dist[next.to] = newCost;
                    pq.offer(new Node(next.to, newCost));
                }
            }
        }
        
        return dist;
    }
}