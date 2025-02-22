import heapq

def solution(jobs):
    finished = 0
    before_job = -1
    now = 0
    answer = 0
    heap = []
    while finished < len(jobs):
        for job in jobs:
            if before_job < job[0] <= now:
                heapq.heappush(heap,[job[1], job[0]])
        
        if heap:
            current_job = heapq.heappop(heap)
            before_job = now
            now += current_job[0]
            answer += now - current_job[1]
            finished += 1
        else:
            now += 1
    return answer // len(jobs)