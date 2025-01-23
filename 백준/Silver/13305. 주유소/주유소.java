import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main{
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine()," ");
        long[] distance = new long[N];
        long[] cost = new long[N];
        for(int i = 0; i < N-1; i++) {
            distance[i] = Long.parseLong(st.nextToken());
        }
        st = new StringTokenizer(br.readLine()," ");
        for(int i = 0; i < N; i++) {
            cost[i] = Long.parseLong(st.nextToken());
        }
        
        long sum = 0;
        long minCost = cost[0];
        
        for(int i = 0; i < N; i++) {
            if(cost[i] < minCost) {
                minCost = cost[i];
            }
            
            sum += minCost * distance[i];
        }
        System.out.println(sum);
    }
}