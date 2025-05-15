import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashSet;

class Solution
{   
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T=Integer.parseInt(br.readLine());

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int ans = 0;
            
            HashSet<String> set = new HashSet<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            
            st = new StringTokenizer(br.readLine());
            for(int i=0; i<N; i++) {
                set.add(st.nextToken());
            }
            
            st = new StringTokenizer(br.readLine());
            for(int i=0; i<M; i++) {
                if(set.contains(st.nextToken())) ans++;
            }
            
            System.out.println("#" + test_case +" "+ ans);
		}
	}
}