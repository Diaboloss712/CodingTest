T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    answer = []
    farming_map = []
    for i in range(N):
        farming_map.append(list(map(int, input())))
    for i in range(N):
        target = N//2
        if i <= N//2:
            answer.extend(farming_map[i][(target-i):(target+i+1)])
        else:
            answer.extend(farming_map[i][(i-target):(N-i+target)])

    print(f'#{test_case} {sum(answer)}')