import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int count = 0;
        int steps = 0;

        ArrayDeque<Board> board = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N * 2; i++) {
            board.add(new Board(Integer.parseInt(st.nextToken())));
        }

        while (count < K) {
            board.addFirst(board.pollLast());

            Iterator<Board> it = board.iterator();
            for (int i = 0; i < N - 1; i++) it.next();
            Board down = it.next();
            down.exist = false;

            Board[] arr = board.toArray(new Board[0]);
            for (int i = N - 2; i >= 0; i--) {
                if (arr[i].exist) {
                    Board next = arr[i + 1];
                    if (!next.exist && next.health > 0) {
                        arr[i].exist = false;
                        next.exist = true;
                        next.health--;
                        if (next.health == 0) count++;
                    }
                }
            }
            arr[N - 1].exist = false;

            Board up = board.getFirst();
            if (!up.exist && up.health > 0) {
                up.exist = true;
                up.health--;
                if (up.health == 0) count++;
            }

            steps++;
        }

        System.out.println(steps);
    }

    static class Board {
        int health;
        boolean exist = false;
        public Board(int health) { this.health = health; }
    }
}
