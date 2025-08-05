import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int answer = 0;

        st = new StringTokenizer(br.readLine());
        int[] tree = new int[N];

        int top = 0;
        for (int i = 0; i < N; i++) {
            tree[i] = Integer.parseInt(st.nextToken());
            if (tree[i] > top)
                top = tree[i];
        }

        int bottom = 0;
        while (bottom <= top) {
            int middle = (top + bottom) / 2;
            long sum = 0;
            for (int j = 0; j < N; j++) {
                if (tree[j] > middle)
                    sum += tree[j] - middle;
            }

            if (sum < M) {
                top = middle - 1;
            } else {
                answer = middle;
                bottom = middle + 1;
            }
        }

        System.out.println(answer);
    }
}
