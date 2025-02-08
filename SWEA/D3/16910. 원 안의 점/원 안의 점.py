T = int(input())
for test_case in range(1,T+1):
    N=int(input())
    answer = 0
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if i**2 + j**2 <=N**2:
                answer += 1
    print(f'#{test_case} {answer}')