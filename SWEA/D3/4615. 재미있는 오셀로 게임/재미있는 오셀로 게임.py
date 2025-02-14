dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
 
 
def check(x_pos, y_pos, color):
    global board
    global N
    for direction in range(8):
        stack = [] * N
        size = 1
        nx = x_pos + dx[direction] * size
        ny = y_pos + dy[direction] * size
        if ny >= N or ny < 0:
            continue
        if nx >= N or nx < 0:
            continue
        if abs(board[ny][nx] - board[y_pos][x_pos]):
            while (0 <= nx < N) and (0 <= ny < N):
                if board[ny][nx] == 5:
                    break
                if board[ny][nx] == board[y_pos][x_pos]:
                    while stack:
                        change_x, change_y = stack.pop()
                        board[change_y][change_x] = color
                    break
                mini = [nx, ny]
                size += 1
                nx = x_pos + dx[direction] * size
                ny = y_pos + dy[direction] * size
                stack.append(mini)
 
 
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    black = 0
    white = 0
    board = [[5] * N for _ in range(N)]
    board[N//2][N//2] = 2
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    for i in range(M):
        x, y, user = list(map(int, input().split()))
        board[y-1][x-1] = user
        check(x-1, y-1, user)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{test_case} {black} {white}')