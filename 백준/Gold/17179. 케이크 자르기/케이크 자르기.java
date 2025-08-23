import java.io.*;
import java.util.*;

class Main {
    public static void main(String args[]) throws IOException {
        int N, M, L;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        
        int[] pos = new int[M+1];
        int[] cutting = new int[N];
        
        for (int i = 0; i < M; i++) {
            pos[i] = Integer.parseInt(br.readLine());
        }
        pos[M] = L;
        Arrays.sort(pos);
        
        for (int j = 0; j < N; j++) {
            cutting[j] = Integer.parseInt(br.readLine());
        }

        StringBuilder sb = new StringBuilder();
        int start, end, mid, curPos, count, answer;

        for (int cut : cutting) {
            answer = 0;
            start = 1;
            end = L;
            while (start <= end) {
                curPos = 0;
                count = 0;
                mid = (start + end) / 2;

                for (int position : pos) {
                    if (position - curPos >= mid) {
                        count += 1;
                        curPos = position;
                    }
                }

                if (count >= cut + 1) {
                    answer = mid;
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
            sb.append(answer).append('\n');
        }
        System.out.print(sb);
    }
}
