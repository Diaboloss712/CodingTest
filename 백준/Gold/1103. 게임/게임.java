import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static int N,M;
    static int[][] map;
    static int[][] dp;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int hole = -99;
    static boolean flag = false;
    static int max = Integer.MIN_VALUE;
    static boolean[][] isvisited;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        dp = new int[N][M];
        isvisited = new boolean[N][M];

        for(int i = 0; i < N; i++) {
            String[] tstring = br.readLine().split("");
            for(int j = 0; j < tstring.length; j++) {
                if(tstring[j].equals("H"))
                    map[i][j] = hole;
                else map[i][j] = Integer.parseInt(tstring[j]);
            }
        }
        isvisited[0][0] = true;
        dfs(0,0,1);
        if(flag) System.out.println(-1);
        else System.out.println(max);
    }

    static void dfs(int x, int y, int cnt){
        if(cnt > max) max = cnt;
        dp[x][y] = cnt;

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i]*map[x][y];
            int ny = y + dy[i]*map[x][y];

            if(nx < 0 || ny < 0 || nx > N-1 || ny > M-1 || map[nx][ny] == hole) {
                continue;
            }

            if(isvisited[nx][ny]) {
                flag = true;
                return;
            }

            if(dp[nx][ny] > cnt) continue;

            isvisited[nx][ny]= true;
            dfs(nx, ny, cnt+1);
            isvisited[nx][ny]= false;
        }
    }
}