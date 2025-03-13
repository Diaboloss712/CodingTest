T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    answer = 0
    conf_time = []
    cur_time = 24
    for i in range(N):
        start, end = input().split()
        conf_time.append(list(map(lambda x: int(x), (start, end))))
    conf_time.sort(key=lambda x: (x[0], x[1]))
    while conf_time:
        start, end = conf_time.pop()
        if end > cur_time:
            continue
        else:
            cur_time = start
            answer += 1
    print(f'#{test_case} {answer}')
