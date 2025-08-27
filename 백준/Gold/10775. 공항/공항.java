import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        int G = Integer.parseInt(br.readLine().trim());
        int P = Integer.parseInt(br.readLine().trim());

        TreeSet<Integer> treeSet = new TreeSet<>();
        for (int i = 1; i <= G; i++) treeSet.add(i);

        int count = 0;
        for (int i = 0; i < P; i++) {
            int g = Integer.parseInt(br.readLine().trim());
            Integer x = treeSet.floor(g);
            if (x == null) break;
            treeSet.remove(x);
            count++;
        }

        out.append(count);
        System.out.println(out);
    }
}
