import java.util.*;

class Solution {

    private int[] dx = {-1, 0, 1, 0};
    private int[] dy = {0, 1, 0, -1};

    public int solution(int[][] maps) {

        int n = maps.length;
        int m = maps[0].length;

        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0,0));

        while(!q.isEmpty()){

            Node cur = q.poll();

            int x = cur.x;
            int y = cur.y;

            for(int i=0;i<4;i++){

                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || ny < 0 || nx >= m || ny >= n)
                    continue;

                if(maps[ny][nx] == 0)
                    continue;

                if(maps[ny][nx] == 1){
                    maps[ny][nx] = maps[y][x] + 1;
                    q.add(new Node(nx,ny));
                }
            }
        }

        int answer = maps[n-1][m-1];

        if(answer == 1)
            return -1;

        return answer;
    }

    static class Node{
        int x;
        int y;

        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}