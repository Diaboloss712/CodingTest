import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] a = new int[N];
        for (int i = 0; i < N; i++) a[i] = Integer.parseInt(br.readLine());

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < k; i++) {
            map.put(a[i], map.getOrDefault(a[i], 0) + 1);
        }

        int answer = map.size() + (map.containsKey(c) ? 0 : 1);

        for (int i = 1; i < N; i++) {
            int out = a[i - 1];
            int cntOut = map.get(out) - 1;
            if (cntOut == 0) map.remove(out);
            else map.put(out, cntOut);

            int in = a[(i + k - 1) % N];
            map.put(in, map.getOrDefault(in, 0) + 1);

            int cur = map.size() + (map.containsKey(c) ? 0 : 1);
            answer = Math.max(answer, cur);

            if (answer == k + 1) break;
        }

        System.out.println(answer);
    }
}
