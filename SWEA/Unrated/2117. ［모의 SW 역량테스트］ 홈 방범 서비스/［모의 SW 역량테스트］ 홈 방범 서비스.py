answer = 0
def search(x, y, distance):
    global answer
    cost = 0
    if distance < 1:
        return
    for k in range(N):
        for l in range(N):
            if (abs(x-l) + abs(y-k) <= distance-1) and board[k][l] == 1:
                cost += 1
            else:
                continue
    if cost * M >= (distance) ** 2 + (distance-1) ** 2:
        if cost > answer:
            answer = cost
    else:
        return search(x, y, distance-1)


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            search(j, i, N*2)
    if answer == 0:
        answer = 1
    print(f'#{test_case} {answer}')
