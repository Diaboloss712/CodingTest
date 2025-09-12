import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder out;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        out = new StringBuilder();

        long A = Integer.parseInt(st.nextToken());
        long B = Integer.parseInt(st.nextToken());
        long C = Integer.parseInt(st.nextToken());

        long result = 1;
        long base = A % C;

        for (long mask = B; mask > 0; mask >>= 1) {
            if ((mask & 1) == 1) {
                result = (result * base) % C;
            }
            base = (base * base) % C;
        }

        out.append(result);
        System.out.println(out);
    }
}
