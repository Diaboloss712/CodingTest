import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());

        int[] qs = new int[T];
        int maxN = 0;
        for (int t = 0; t < T; t++) {
            qs[t] = Integer.parseInt(br.readLine().trim());
            if (qs[t] > maxN) maxN = qs[t];
        }

        int[] dp = new int[maxN + 1];
        dp[0] = 1;

        int[] coins = {1, 2, 3};
        for (int c : coins) {
            for (int i = c; i <= maxN; i++) {
                dp[i] += dp[i - c];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int n : qs) {
            sb.append(dp[n]).append('\n');
        }
        System.out.print(sb.toString());
    }
}
