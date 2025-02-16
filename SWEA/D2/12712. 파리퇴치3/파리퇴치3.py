dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def plus_kill(x,y):
    global M
    global board
    global answer
    plus_max = 0
    for direction in range(0,8,2):
        cur_max = 0
        for size in range(1, M):
            nx = x + dx[direction]*size
            ny = y + dy[direction]*size
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                break
            cur_max += board[ny][nx]
        plus_max += cur_max
    if answer < plus_max + board[y][x]:
        answer = plus_max + board[y][x]
    return


def multiply_kill(x,y):
    global M
    global board
    global answer
    multiply_max = 0
    for direction in range(1,8,2):
        cur_max = 0
        for size in range(1, M):
            nx = x + dx[direction]*size
            ny = y + dy[direction]*size
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                break
            cur_max += board[ny][nx]
        multiply_max += cur_max
    if answer < multiply_max + board[y][x]:
        answer = multiply_max + board[y][x]
    return


T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    board = [[0] * N for _ in range(N)]
    answer = 0
    for i in range(N):
        board[i] = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            plus_kill(j,i)
            multiply_kill(j,i)
    print(f'#{test_case} {answer}')
