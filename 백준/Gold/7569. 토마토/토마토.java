import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder out;
    static int count;
    static int target;
    static boolean[][][] visited;
    static int[][][] graph;

    static int N, M, H;

    static class Node implements Comparable<Node> {
        int x;
        int y;
        int z;
        int day;

        public Node(int x, int y, int z, int day) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.day = day;
        }

        @Override
        public int compareTo(Node o) {
            return this.day - o.day;
        }
    }

    static int[] dx;
    static int[] dy;
    static int[] dz;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        out = new StringBuilder();

        List<Node> arr = new ArrayList<>();

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        dx = new int[]{-1, 0, 1, 0};
        dy = new int[]{0, -1, 0, 1};
        dz = new int[]{-1, 1};

        count = 0;
        target = N*M*H;

        graph = new int[N][M][H];
        visited = new boolean[N][M][H];
        for(int height = 0; height < H; height++) {
            for(int row = 0; row < N; row++) {
                st = new StringTokenizer(br.readLine());
                for(int column = 0; column < M; column++) {
                    graph[row][column][height] = Integer.parseInt(st.nextToken());
                    if(graph[row][column][height] == 1) {
                        arr.add(new Node(column, row, height, 0));
                        count += 1;
                        visited[row][column][height] = true;
                    }
                    if(graph[row][column][height] == -1) {
                        target -= 1;
                    }
                }
            }
        }
        if(target == count){
            out.append("0\n");
            System.out.println(out);
            return;
        }
        int answer = bfs(arr);
        if(count != target) {
            out.append("-1\n");
        }
        else {
            out.append(answer);
        }
        System.out.println(out);
    }

    static int bfs(List<Node> arr) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.addAll(arr);
        int lastDay = 0;

        while(!pq.isEmpty()) {
            Node curNode = pq.poll();
            int curX = curNode.x;
            int curY = curNode.y;
            int curZ = curNode.z;
            int day = curNode.day;
            lastDay = day;

            for(int i = 0; i < 4; i++) {
                int nextX = curX + dx[i];
                int nextY = curY + dy[i];
                int nextZ = curZ;
                if(nextX >= M || nextX < 0 || nextY >= N || nextY < 0) {
                    continue;
                }
                if(visited[nextY][nextX][nextZ] || graph[nextY][nextX][nextZ] == -1) {
                    continue;
                }
                pq.add(new Node(nextX, nextY, nextZ, day+1));
                visited[nextY][nextX][nextZ] = true;
                count++;
            }
            for(int i = 0; i < 2; i++) {
                int nextX = curX;
                int nextY = curY;
                int nextZ = curZ + dz[i];
                if(nextZ >= H || nextZ < 0) {
                    continue;
                }
                if(visited[nextY][nextX][nextZ] || graph[nextY][nextX][nextZ] == -1) {
                    continue;
                }
                pq.add(new Node(nextX, nextY, nextZ, day+1));
                visited[nextY][nextX][nextZ] = true;
                count++;
            }
        }
        return lastDay;
    }
}
