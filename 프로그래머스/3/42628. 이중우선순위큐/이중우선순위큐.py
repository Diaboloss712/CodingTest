import heapq

def solution(operations):
    min_q = []
    max_q = []
    answer = []
    for operation in operations:
        order, num = operation.split()
        if order == 'I':
            heapq.heappush(min_q, int(num))
            heapq.heappush(max_q, -int(num))
        else:
            if min_q:
                if num == '1':
                    min_q.remove(-heapq.heappop(max_q))
                else:
                    max_q.remove(-heapq.heappop(min_q))
    if not min_q:
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(max_q), heapq.heappop(min_q)]
    return answer