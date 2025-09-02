import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static final int INF = 10000001;
    static StringTokenizer st;
    static BufferedReader br;
    static int N;
    static int count = 0;
    static int[][] map;
    static int[][] distance;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        
        while(true) {
            st = new StringTokenizer(br.readLine());
            count++;

            N = Integer.parseInt(st.nextToken());
            distance = new int[N][N];
            visited = new boolean[N][N];
            map = new int[N][N];

            if (N == 0) {
                System.out.println(out);
                return;
            }

            for(int i = 0; i < N; i++)
                Arrays.fill(distance[i], INF);

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            out.append("Problem ").append(count).append(": ").append(dijkstra(map[0][0])).append("\n");
        }
    }
    static int dijkstra(int penalty) {
        PriorityQueue<Near> queue = new PriorityQueue<>();
        Near startNear = new Near(0, 0, penalty);
        queue.add(startNear);

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        while(!queue.isEmpty()) {
            Near cur = queue.poll();
            int start = cur.start;
            int end = cur.end;
            if(visited[start][end])
                continue;
            visited[start][end] = true;

            if(start == N-1 && end == N-1)
                return cur.distance;

            for (int k = 0; k < 4; k++) {
                int nextX = start + dx[k];
                int nextY = end + dy[k];
                if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= N) continue;

                int nextDistance = cur.distance + map[nextX][nextY];
                if (!visited[nextX][nextY] && nextDistance < distance[nextX][nextY]) {
                    distance[nextX][nextY] = nextDistance;
                    queue.add(new Near(nextX, nextY, nextDistance));
                }
            }
        }
        return distance[N - 1][N - 1];
    }

    static class Near implements Comparable<Near> {
        int start;
        int end;
        int distance;
        public Near(int start, int end, int distance) {
            this.start = start;
            this.end = end;
            this.distance = distance;
        }

        @Override
        public int compareTo(Near o) {
            return this.distance - o.distance;
        }
    }
}
