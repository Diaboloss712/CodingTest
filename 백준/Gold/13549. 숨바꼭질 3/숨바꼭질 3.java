import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.Comparator;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        
        int answer = bfs(N, X);
        System.out.println(answer);
    }
    
    public static int bfs(int start, int end) {
        final int MAX = 100000;
        int[] dist = new int[MAX + 1];
        for (int i = 0; i <= MAX; i++) dist[i] = Integer.MAX_VALUE;

        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        
        queue.add(new int[] {start, 0});
        dist[start] = 0;
        
        while (!queue.isEmpty()) {
            int[] data = queue.poll();
            int pos = data[0];
            int time = data[1];
            
            if (pos == end) {
                return time;
            }
            if (time > dist[pos]) continue;

            if (pos * 2 <= MAX && time < dist[pos * 2]) {
                dist[pos * 2] = time;
                queue.add(new int[] {pos * 2, time});
            }
            if (pos + 1 <= MAX && time + 1 < dist[pos + 1]) {
                dist[pos + 1] = time + 1;
                queue.add(new int[] {pos + 1, time + 1});
            }
            if (pos - 1 >= 0 && time + 1 < dist[pos - 1]) {
                dist[pos - 1] = time + 1;
                queue.add(new int[] {pos - 1, time + 1});
            }
        }
        return -1;
    }
}
