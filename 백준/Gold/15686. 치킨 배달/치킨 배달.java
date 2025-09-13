import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;

    static int[][] board;
    static int N, M;
    static List<int[]> homes;
    static List<int[]> chickens;
    static int answer;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][N];
        homes = new ArrayList<>();
        chickens = new ArrayList<>();
        answer = Integer.MAX_VALUE;

        for (int row = 0; row < N; row++) {
            st = new StringTokenizer(br.readLine());
            for (int column = 0; column < N; column++) {
                board[row][column] = Integer.parseInt(st.nextToken());
                if (board[row][column] == 1) homes.add(new int[]{row, column});
                if (board[row][column] == 2) chickens.add(new int[]{row, column});
            }
        }

        comb(0, 0, new ArrayList<>());
        System.out.println(answer);
    }

    static void comb(int idx, int cnt, List<int[]> selected) {
        if (cnt == M) {
            int dist = getCityDist(selected);
            answer = Math.min(answer, dist);
            return;
        }
        if (idx >= chickens.size()) return;

        selected.add(chickens.get(idx));
        comb(idx + 1, cnt + 1, selected);
        selected.remove(selected.size() - 1);

        comb(idx + 1, cnt, selected);
    }

    static int getCityDist(List<int[]> selected) {
        int sum = 0;
        for (int[] home : homes) {
            int minDist = Integer.MAX_VALUE;
            for (int[] chick : selected) {
                int d = Math.abs(home[0] - chick[0]) + Math.abs(home[1] - chick[1]);
                if (d < minDist) minDist = d;
            }
            sum += minDist;
        }
        return sum;
    }
}
