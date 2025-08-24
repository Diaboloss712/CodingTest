import java.io.*;
import java.util.*;

public class Main {

    static final int INF = 1_000_000_000;

    static class Edge {
        int to, w;
        Edge(int to, int w) { this.to = to; this.w = w; }
    }
    static class State implements Comparable<State> {
        int v, dist;
        State(int v, int dist) { this.v = v; this.dist = dist; }
        @Override public int compareTo(State o) {
            return Integer.compare(this.dist, o.dist);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            List<List<Edge>> adj = new ArrayList<>(n + 1);
            for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());

            for (int i = 0; i < d; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int s = Integer.parseInt(st.nextToken());
                adj.get(b).add(new Edge(a, s)); // b 감염 후 s초 뒤 a 감염
            }

            int[] dist = dijkstra(adj, c, n);

            int infected = 0, maxTime = 0;
            for (int i = 1; i <= n; i++) {
                if (dist[i] != INF) {
                    infected++;
                    if (dist[i] > maxTime) maxTime = dist[i];
                }
            }
            out.append(infected).append(' ').append(maxTime).append('\n');
        }
        System.out.print(out);
    }

    static int[] dijkstra(List<List<Edge>> adj, int start, int n) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, INF);
        PriorityQueue<State> pq = new PriorityQueue<>();

        dist[start] = 0;
        pq.offer(new State(start, 0));

        while (!pq.isEmpty()) {
            State cur = pq.poll();
            if (cur.dist != dist[cur.v]) continue; // stale 상태 스킵

            for (Edge e : adj.get(cur.v)) {
                int nd = cur.dist + e.w;
                if (nd < dist[e.to]) {
                    dist[e.to] = nd;
                    pq.offer(new State(e.to, nd));
                }
            }
        }
        return dist;
    }
}
