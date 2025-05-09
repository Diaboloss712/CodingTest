import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
    static long MOD = 998244353;
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T=Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
            String B = br.readLine();
            String word = br.readLine();
            int BASE = 131;
            int count = 0;
            long hashNum = 0;
            long[] pow = new long[word.length()];
            pow[0] = 1;
            for (int i = 1; i < word.length(); i++) {
                pow[i] = (pow[i - 1] * BASE) % MOD;
            }
            for(int i = 0; i < word.length(); i++){
                hashNum =(hashNum + ((long)word.charAt(i) * pow[word.length() - i - 1]) % MOD) % MOD;
            }
            long startHash = 0;
            for(int j = 0; j < word.length(); j++) {
                startHash = (startHash + ((long)B.charAt(j) * pow[(word.length() - j - 1)] % MOD)) % MOD;
            }
            if (startHash == hashNum) {
                count++;
            }
            for(int i = 0; i < B.length() - word.length(); i++) {
                long remove = (B.charAt(i) * pow[word.length() - 1]) % MOD;
				startHash = (startHash - remove + MOD) % MOD;
				startHash = (startHash * BASE) % MOD;
				startHash = (startHash + B.charAt(i + word.length())) % MOD;
                if (startHash == hashNum) {
                    count++;
                }
            }
            System.out.println("#" + test_case +" "+ count);
		}
	}
}