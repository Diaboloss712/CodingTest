import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static int N, ALL, answer;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        ALL = (1 << N) - 1;
        answer = 0;

        dfs(0, 0, 0, 0);
        System.out.println(answer);
    }

    static void dfs(int row, int cols, int d1, int d2) {
        if (row == N) {
            answer++;
            return;
        }
        int available = ALL & ~(cols | d1 | d2);
        while (available != 0) {
            int pick = available & -available;
            available -= pick;
            dfs(row + 1, cols | pick, ((d1 | pick) << 1) & ALL, (d2 | pick) >> 1);
        }
    }
}
