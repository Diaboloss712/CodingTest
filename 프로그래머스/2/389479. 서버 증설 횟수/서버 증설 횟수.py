import heapq


def solution(players, m, k):
    q = []
    answer = 0
    time = 0
    for player in players:
        cur_req_server = player // m
        while q:
            if q[0] <= time:
                heapq.heappop(q)
            else:
                break
        while len(q) < cur_req_server:
            heapq.heappush(q, time + k)
            answer += 1
        time += 1
    return answer