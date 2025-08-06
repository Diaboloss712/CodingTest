import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int[] visitor = new int[N];
        int[] sum = new int[N];
        int max = 0;
        int count = 1;
        
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            visitor[i] = Integer.parseInt(st.nextToken());
            sum[i] = 0;
        }
        sum[0] = visitor[0];
        
        for(int i = 1; i < N; i++) {
            sum[i] += sum[i-1] + visitor[i];
            if(i >= X) {
                sum[i] -= visitor[i-X];
            }
            if(sum[i] > max) {
                max = sum[i];
                count = 1;
            }
            else if(sum[i] == max) {
                count += 1;
            }
        }
        if(max == 0)
            System.out.println("SAD");
        else {
            System.out.println(max);
            System.out.println(count);
        }
    }
}