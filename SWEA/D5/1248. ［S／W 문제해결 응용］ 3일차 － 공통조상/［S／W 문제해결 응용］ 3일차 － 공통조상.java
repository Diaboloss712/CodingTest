import java.io.*;
import java.util.*;

public class Solution {

    static class Node {
        int data;
        int parentIdx;
        int leftChildIdx;
        int rightChildIdx;
        int depth;

        Node(int data) {
            this.data = data;
        }
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static Node[] nodes;
    static int V, E, a, b;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            nodes = new Node[V + 1];
            for (int i = 1; i <= V; i++) {
                nodes[i] = new Node(i);
            }

            st = new StringTokenizer(in.readLine());
            for (int i = 0; i < E; i++) {
                int parent = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());
                if (nodes[parent].leftChildIdx == 0)
                    nodes[parent].leftChildIdx = child;
                else
                    nodes[parent].rightChildIdx = child;
                nodes[child].parentIdx = parent;
            }

            dfsSetDepth(1, 0);

            int lca = findLCA(a, b);
            int size = getSubtreeSize(lca);

            sb.append("#").append(tc).append(" ").append(lca).append(" ").append(size).append("\n");
        }

        System.out.print(sb);
    }

    static void dfsSetDepth(int current, int depth) {
        nodes[current].depth = depth;
        if (nodes[current].leftChildIdx != 0)
            dfsSetDepth(nodes[current].leftChildIdx, depth + 1);
        if (nodes[current].rightChildIdx != 0)
            dfsSetDepth(nodes[current].rightChildIdx, depth + 1);
    }

    static int findLCA(int x, int y) {
        while (nodes[x].depth > nodes[y].depth) x = nodes[x].parentIdx;
        while (nodes[y].depth > nodes[x].depth) y = nodes[y].parentIdx;
        while (x != y) {
            x = nodes[x].parentIdx;
            y = nodes[y].parentIdx;
        }
        return x;
    }

    static int getSubtreeSize(int current) {
        int size = 1;
        if (nodes[current].leftChildIdx != 0)
            size += getSubtreeSize(nodes[current].leftChildIdx);
        if (nodes[current].rightChildIdx != 0)
            size += getSubtreeSize(nodes[current].rightChildIdx);
        return size;
    }
}