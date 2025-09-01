import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long[] arr;
    static long[] seg;

    static void init(int start, int end, int pos) {
        if(start == end) {
            seg[pos] = arr[start];
            return;
        }
        int mid = (start + end) / 2;
        init(start, mid, pos*2);
        init(mid+1, end, pos*2+1);
        seg[pos] = seg[pos*2] + seg[pos*2+1];
    }

    static void update(int start, int end, int pos, long value, int index) {
        if(start == end) {
            seg[pos] = value;
            return;
        }
        int mid = (start + end) / 2;
        if(index <= mid)
            update(start, mid, pos*2, value, index);
        else update(mid+1, end, pos*2+1, value, index);
        seg[pos] = seg[pos*2] + seg[pos*2+1];
    }

    static long query(int start, int end, int pos, int left, int right) {
        if (right < start || end < left) return 0L;
        if (left <= start && end <= right) return seg[pos];
        int mid = (start + end) / 2;
        return query(start, mid, pos * 2, left, right)
                + query(mid + 1, end, pos * 2 + 1, left, right);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        arr = new long[N + 1];
        seg = new long[4 * N + 5];

        for (int i = 1; i <= N; i++) {
            arr[i] = Long.parseLong(br.readLine().trim());
        }

        init(1, N, 1);

        StringBuilder out = new StringBuilder();
        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if (a == 1) {
                update(1, N, 1, c, b);
                arr[b] = c;
            } else {
                int l = b;
                int r = (int) c;
                if (l > r) { int tmp = l; l = r; r = tmp; }
                out.append(query(1, N, 1, l, r)).append('\n');
            }
        }
        System.out.print(out.toString());
    }
}
