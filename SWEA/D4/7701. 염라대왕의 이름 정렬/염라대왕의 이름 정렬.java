import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
		int T = Integer.parseInt(br.readLine());
        
		for(int test_case = 1; test_case <= T; test_case++)
		{
            System.out.println("#"+test_case);
            HashMap<String, String> map = new HashMap<>();
            int N = Integer.parseInt(br.readLine());
            for(int i = 0; i < N; i++){
                String s = br.readLine();
                map.put(s, s);
            }
            map.values().stream()
                .sorted(Comparator.comparingInt(String::length)
                        .thenComparing(Comparator.naturalOrder()))
                .forEach(System.out::println);
		}
	}
}