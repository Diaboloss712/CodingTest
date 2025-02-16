import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(board, x, y, chance, depth):
    global K
    global answer
    for direction in range(4):
        nx = dx[direction] + x
        ny = dy[direction] + y
        if 0 > nx or N <= nx or 0 > ny or N <= ny or visited[ny][nx]:
            continue
        if board[ny][nx] >= board[y][x]:
            if chance and board[ny][nx] - K < board[y][x]:
                new_board = copy.deepcopy(board)
                new_board[ny][nx] = board[y][x]-1
                visited[ny][nx] = 1
                dfs(new_board, nx, ny, chance-1, depth+1)
                visited[ny][nx] = 0
            else:
                if answer < depth:
                    answer = depth
                continue
        else:
            visited[ny][nx] = 1
            dfs(board, nx, ny, chance, depth+1)
            visited[ny][nx] = 0
    return

T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N, K = list(map(int, input().split()))
    board = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start = 0
    for i in range(N):
        board[i] = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            if board[i][j] > start:
                start = board[i][j]
    for i in range(N):
        for j in range(N):
            if board[i][j] == start:
                visited[i][j] = 1
                dfs(board, j, i, 1, 1)
                visited[i][j] = 0
    print(f'#{test_case} {answer}')