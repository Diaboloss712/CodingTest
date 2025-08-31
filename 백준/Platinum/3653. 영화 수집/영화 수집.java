import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int SIZE, top;
    static int[] seg, arr, posArr;

    static void init(int pos, int start, int end) {
        if (start == end) { seg[pos] = arr[start]; return; }
        int mid = (start + end) / 2;
        init(pos * 2, start, mid);
        init(pos * 2 + 1, mid + 1, end);
        seg[pos] = seg[pos * 2] + seg[pos * 2 + 1];
    }

    static void update(int pos, int start, int end, int idx, int val) {
        if (start == end) { seg[pos] = val; return; }
        int mid = (start + end) / 2;
        if (idx <= mid) update(pos * 2, start, mid, idx, val);
        else update(pos * 2 + 1, mid + 1, end, idx, val);
        seg[pos] = seg[pos * 2] + seg[pos * 2 + 1];
    }

    static int query(int pos, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return seg[pos];
        int mid = (start + end) / 2;
        return query(pos * 2, start, mid, l, r) + query(pos * 2 + 1, mid + 1, end, l, r);
    }

    static void initTree(int size) {
        SIZE = size;
        seg = new int[4 * (SIZE + 5)];
        arr = new int[SIZE + 1];
        init(1, 1, SIZE);
    }

    static void pointUpdate(int idx, int val) {
        update(1, 1, SIZE, idx, val);
    }

    static int countAbove(int p) {
        return query(1, 1, SIZE, 1, p - 1);
    }

    public static void main(String[] args) throws Exception {
        StringBuilder out = new StringBuilder();

        while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        while (T-- > 0) {
            while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            if (!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());

            initTree(N + M);
            posArr = new int[N + 1];
            top = M;

            for (int i = 1; i <= N; i++) {
                posArr[i] = M + i;
                pointUpdate(posArr[i], 1);
            }

            for (int q = 0; q < M; q++) {
                while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());

                out.append(countAbove(posArr[x])).append('\n');
                pointUpdate(posArr[x], 0);
                pointUpdate(top, 1);
                posArr[x] = top;
                top--;
            }
        }
        System.out.print(out);
    }
}
