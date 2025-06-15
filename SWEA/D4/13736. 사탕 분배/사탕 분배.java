import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T=Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
		
			StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            System.out.printf("#%d %d\n", test_case, solution(A, B, K));
		}
	}
    
    static long solution(int A, int B, int K) {
        int sum = A + B;
        int max = sum / 2;
        long result = ((long)getPow(K, sum) * (long)A) % sum;
        return result > max ? sum - result : result;
    }
    
    static int getPow(int K, int mod) {
        long res = 1;
        long num = 2;
        while (K > 0) {
            if (K % 2 == 1) {
                res = (res * num) % mod;
            }
            num = (num * num) % mod;
            K /= 2;
        }
        return (int)res;
    }
}