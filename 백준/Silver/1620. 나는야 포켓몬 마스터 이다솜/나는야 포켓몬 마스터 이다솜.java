import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static Map<Integer, String> strmap;
    static Map<String, Integer> intmap;
    static StringBuilder out;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        out = new StringBuilder();

        strmap = new HashMap<>();
        intmap = new HashMap<>();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        for(int i = 1; i <= N; i++) {
            String monster = br.readLine();
            intmap.put(monster, i);
            strmap.put(i, monster);
        }
        for(int i = 1; i <= M; i++) {
            String target = br.readLine();
            if(intmap.get(target) == null) {
                out.append(strmap.get(Integer.parseInt(target))).append("\n");
            }
            else {
                out.append(intmap.get(target)).append("\n");
            }
        }
        System.out.println(out);
    }
}
