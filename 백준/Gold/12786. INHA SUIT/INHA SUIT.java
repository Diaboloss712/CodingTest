import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 1_000_000_000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());

        List<int[]> holes = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int[] arr = new int[M];
            for (int j = 0; j < M; j++) arr[j] = Integer.parseInt(st.nextToken());
            holes.add(arr);
        }

        int[][] dp = new int[N+1][21];
        for (int i = 0; i <= N; i++) Arrays.fill(dp[i], INF);
        dp[0][1] = 0;

        for (int i = 0; i < N; i++) {
            int[] cur = holes.get(i);
            for (int h = 1; h <= 20; h++) {
                if (dp[i][h] == INF) continue;

                Set<Integer> nextSet = new HashSet<>();
                nextSet.add(h);
                if (h+1 <= 20) nextSet.add(h+1);
                if (h-1 >= 1) nextSet.add(h-1);
                if (h < 10) nextSet.add(Math.min(20, h*2));
                else nextSet.add(20);

                boolean matched = false;
                for (int nh : cur) {
                    if (nextSet.contains(nh)) {
                        dp[i+1][nh] = Math.min(dp[i+1][nh], dp[i][h]);
                        matched = true;
                    }
                }
                if (!matched && dp[i][h] < K) {
                    for (int nh : cur) {
                        dp[i+1][nh] = Math.min(dp[i+1][nh], dp[i][h]+1);
                    }
                }
            }
        }

        int ans = INF;
        for (int h = 1; h <= 20; h++) ans = Math.min(ans, dp[N][h]);
        System.out.println(ans == INF ? -1 : ans);
    }
}
