import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br;
    static StringBuilder out;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int test_case = 0; test_case < T; test_case++) {
            String cmd = br.readLine();
            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), "[],");

            Deque<Integer> dq = new ArrayDeque<>();
            while (st.hasMoreTokens()) {
                dq.add(Integer.parseInt(st.nextToken()));
            }

            boolean reversed = false;
            boolean error = false;

            for (char c : cmd.toCharArray()) {
                if (c == 'R') {
                    reversed = !reversed;
                } else if (c == 'D') {
                    if (dq.isEmpty()) {
                        error = true;
                        break;
                    }
                    if (!reversed) {
                        dq.pollFirst();
                    } else {
                        dq.pollLast();
                    }
                }
            }

            if (error) {
                out.append("error\n");
            } else {
                out.append("[");
                if (!dq.isEmpty()) {
                    if (!reversed) {
                        while (!dq.isEmpty()) {
                            out.append(dq.pollFirst());
                            if (!dq.isEmpty()) out.append(",");
                        }
                    } else {
                        while (!dq.isEmpty()) {
                            out.append(dq.pollLast());
                            if (!dq.isEmpty()) out.append(",");
                        }
                    }
                }
                out.append("]\n");
            }
        }

        System.out.print(out.toString());
    }
}