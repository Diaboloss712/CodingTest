import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int ans = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int food : scoville) {
            pq.add(food);
        }
        while(pq.peek() < K && pq.size() > 1) {
            int min_scoville = pq.poll() + pq.poll()*2;
            pq.add(min_scoville);
            ans++;
        }
        if(pq.peek() < K)
            return -1;
        return ans;
    }
}