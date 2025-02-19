import queue

T = int(input())
for test_case in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    qualifier = list(map(int, input().split()))
    flag = True
    q = queue.PriorityQueue()
    bun_count = 1
    for num in qualifier:
        q.put(num)
    max_time = max(qualifier)
    for time in range(N):
        check = q.get(time)
        if (check//M)*K - bun_count < 0:
            flag = False
            break
        bun_count += 1
    if flag:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')
