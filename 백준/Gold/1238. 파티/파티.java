import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int end, distance;

        Node(int end, int distance) {
            this.end = end;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }
    }

    static BufferedReader br;
    static StringTokenizer st;
    static ArrayList<ArrayList<Node>> arr;
    static int N, M, X;
    static final int INF = 1000000000;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            arr.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int distance = Integer.parseInt(st.nextToken());
            arr.get(start).add(new Node(end, distance));
        }

        int[] distanceList = dijkstra(X);

        int answer = 0;
        for (int i = 1; i <= N; i++) {
            int[] distToX = dijkstra(i);
            int total = distToX[X] + distanceList[i];
            answer = Math.max(answer, total);
        }

        System.out.println(answer);
    }

    static int[] dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        boolean[] visited = new boolean[N + 1];
        int[] dist = new int[N + 1];
        Arrays.fill(dist, INF);

        dist[start] = 0;
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();
            int curPos = curNode.end;

            if (visited[curPos]) continue;
            visited[curPos] = true;

            for (Node next : arr.get(curPos)) {
                if (dist[next.end] > dist[curPos] + next.distance) {
                    dist[next.end] = dist[curPos] + next.distance;
                    pq.add(new Node(next.end, dist[next.end]));
                }
            }
        }
        return dist;
    }
}
