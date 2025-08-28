import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    static StringTokenizer st;

    static class Node {
        String num;
        Node[] node;
        boolean end;

        public Node(String num, Node[] next) {
            this.num = num;
            this.node = (next != null) ? next : new Node[10];
        }
        public Node(String num, Node[] next, boolean end) {
            this.num = num;
            this.node = (next != null) ? next : new Node[10];
            this.end = end;
        }
        public Node(String num) {
            this.num = num;
            this.node = new Node[10];
            this.end = false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            String[] nums = new String[N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                nums[i] = st.nextToken();
            }
            Arrays.sort(nums);
            
            Node[] Trie = new Node[10];
            for (int i = 0; i <= 9; i++) Trie[i] = new Node(String.valueOf(i));

            boolean flag = isFlag(nums, Trie, true);

            if (flag) output.append("YES\n");
            else output.append("NO\n");
        }
        System.out.print(output);
    }

    private static boolean isFlag(String[] nums, Node[] Trie, boolean flag) {
        for (int i = 0; i < nums.length; i++) {
            String phoneNum = nums[i];
            
            Node curNode = Trie[phoneNum.charAt(0) - '0'];
            
            for (int j = 1; j < phoneNum.length(); j++) {
                if (curNode.end) return false;

                int d = phoneNum.charAt(j) - '0';
                if (curNode.node[d] == null) {
                    curNode.node[d] = new Node(String.valueOf(phoneNum.charAt(j)));
                }
                curNode = curNode.node[d];
            }
            
            if (curNode.end) return false;
            curNode.end = true;
        }
        return flag;
    }
}
