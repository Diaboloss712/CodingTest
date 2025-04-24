import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t <= 10; t++) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            ArrayList<Integer> list = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                list.add(Integer.parseInt(st.nextToken()));
            }

            int Q = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());

            for (int i = 0; i < Q; i++) {
                String cmd = st.nextToken();

                if (cmd.equals("I")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++) {
                        list.add(x + j, Integer.parseInt(st.nextToken()));
                    }
                } else if (cmd.equals("D")) {
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++) {
                        if (x < list.size()) list.remove(x);
                    }
                } else if (cmd.equals("A")) {
                    int y = Integer.parseInt(st.nextToken());
                    for (int j = 0; j < y; j++) {
                        list.add(Integer.parseInt(st.nextToken()));
                    }
                }
            }

            sb.append("#").append(t);
            for (int i = 0; i < 10; i++) {
                sb.append(" ").append(list.get(i));
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }
}
