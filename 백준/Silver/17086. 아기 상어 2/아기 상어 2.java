import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder out;

    static int N, M;
    static int[][] board;
    static int[][] dist;
    static int[] dx = {-1,-1,-1,0,1,1,1,0};
    static int[] dy = {-1,0,1,1,1,0,-1,-1};

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        out = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        dist = new int[N][M];

        Deque<int[]> q = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) {
                    q.add(new int[]{i, j});
                    dist[i][j] = 0;
                } else {
                    dist[i][j] = -1;
                }
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            for (int dir = 0; dir < 8; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                if (dist[nx][ny] != -1) continue;
                dist[nx][ny] = dist[x][y] + 1;
                q.add(new int[]{nx, ny});
            }
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                ans = Math.max(ans, dist[i][j]);
            }
        }

        out.append(ans).append("\n");
        System.out.print(out);
    }
}
