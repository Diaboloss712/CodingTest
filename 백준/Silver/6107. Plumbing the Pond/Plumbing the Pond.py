dx = [-1,  0,  1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1,  0, 0,  1, 1, 1]

def check_dir(x, y):
    for direction in range(8):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or ny < 0 or nx >= C or ny >= R:
            continue
        if board[y][x] == board[ny][nx]:
            return board[y][x]
    return 0

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

max_depth = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == 0:
            continue
        num = check_dir(j, i)
        if num:
            max_depth = max(max_depth, num)

print(max_depth)