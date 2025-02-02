import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < N; i++) {
            Stack<Character> leftStack = new Stack<>();
            Stack<Character> rightStack = new Stack<>();
            String input = br.readLine();
            
            for (char c : input.toCharArray()) {
                if (c == '<') {
                    if (!leftStack.isEmpty()) {
                        rightStack.push(leftStack.pop());
                    }
                } else if (c == '>') {
                    if (!rightStack.isEmpty()) {
                        leftStack.push(rightStack.pop());
                    }
                } else if (c == '-') {
                    if (!leftStack.isEmpty()) {
                        leftStack.pop();
                    }
                } else {
                    leftStack.push(c);
                }
            }
            
            StringBuilder sb = new StringBuilder(leftStack.size() + rightStack.size());
            for (char ch : leftStack) {
                sb.append(ch);
            }
            while (!rightStack.isEmpty()) {
                sb.append(rightStack.pop());
            }
            
            bw.write(sb.toString());
            bw.write("\n");
        }
        
        bw.flush();
        bw.close();
    }
}