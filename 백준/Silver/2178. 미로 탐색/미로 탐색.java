import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class Main{
    static int N,M;
    static int[][] map;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static boolean flag = false;
    static boolean[][] visited;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());
        map = new int[N][M];
        visited = new boolean[N][M];
        
        for(int i = 0; i < N; i++) {
            String[] st = br.readLine().split("");
            for(int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st[j]);
            }
        }
        bfs(0,0);
        System.out.println(map[N-1][M-1]);
    }
    
    
    public static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {x,y});
        visited[x][y] = true;
        
        while(!queue.isEmpty()) {
            int[] now = queue.poll();
            
            for(int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];                
                if(0 > nx || nx >= N || 0 > ny || ny >= M)
                    continue;
                if(map[nx][ny]==0 || visited[nx][ny])
                    continue;
                queue.add(new int[] {nx,ny});
                map[nx][ny] = map[now[0]][now[1]]+1;
                visited[nx][ny] = true;
            }
        }
    }
}