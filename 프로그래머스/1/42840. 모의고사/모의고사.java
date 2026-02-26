import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        int p1 = 0;
        int p2 = 0;
        int p3 = 0;
        
        int[] p2answers = {2,1,2,3,2,4,2,5};
        int[] p3answers = {3,3,1,1,2,2,4,4,5,5};
        
        for(int i = 0; i < answers.length; i++) {
            if(i % 5 + 1 == answers[i]) p1++;
            if(p2answers[i % 8] == answers[i]) p2++;
            if(p3answers[i % 10] == answers[i]) p3++;
        }
        
        int max = Math.max(p1, Math.max(p2, p3));
        
        int count = 0;
        if(p1 == max) count++;
        if(p2 == max) count++;
        if(p3 == max) count++;
        
        int[] result = new int[count];
        int idx = 0;
        
        if(p1 == max) result[idx++] = 1;
        if(p2 == max) result[idx++] = 2;
        if(p3 == max) result[idx++] = 3;
        
        return result;
    }
}