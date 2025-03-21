import heapq

T = int(input())
for test_case in range(1, T + 1):
    x_start, x_end, y_start, y_end = list(map(int, input().split()))
    answer = 0
    q = []
    for i in range(100):
        if x_start == i:
            heapq.heappush(q, x_end)
        if y_start == i:
            heapq.heappush(q, y_end)
        if q:
            if q[0] == i:
                break
            elif len(q) == 2:
                answer += 1
    print(f'#{test_case} {answer}')
