import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Set;
import java.util.HashSet;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for(int test_case = 1; test_case <= T; test_case++)
		{
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            Set<Integer> s = new HashSet<>();
            int i = 0;
            while(s.size() < 10) {
                i++;                
                int count_num = N * i;
                while(count_num >= 10) { // 10으로 쪼개서 각자리의 숫자 
                    s.add(count_num % 10);
                    count_num = count_num / 10;
                }
                s.add(count_num % 10);
            }
            System.out.println("#" + test_case + " " + N * i);
		}
	}
}