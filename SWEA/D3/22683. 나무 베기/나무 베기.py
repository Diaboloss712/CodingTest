dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def check_direction(cur_dir, object_dir):
    if cur_dir == object_dir:
        return 1
    elif cur_dir[0] == -1 * object_dir[0] and cur_dir[1] == -1 * object_dir[1]:
        return 3
    else:
        return 2


def dfs(x, y, cost, chance, cur_direction):
    global answer
    global visited
    if cost >= answer:
        return
    if (x, y) == end:
        if answer > cost:
            answer = cost
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visited[ny][nx]:
            continue
        next_cost = check_direction(cur_direction, (dx[direction], dy[direction]))
        if board[ny][nx] == 'T' and chance == 0:
            continue
        elif board[ny][nx] == 'T':
            visited[ny][nx] = 1
            dfs(nx, ny, cost + next_cost, chance - 1, (dx[direction], dy[direction]))
            visited[ny][nx] = 0
        else:
            visited[ny][nx] = 1
            dfs(nx, ny, cost + next_cost, chance, (dx[direction], dy[direction]))
            visited[ny][nx] = 0


T = int(input())
for test_case in range(1, T + 1):
    answer = 1e9
    N, K = list(map(int, input().split()))
    visited = [[0] * N for _ in range(N)]
    board = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                start = (j, i)
            if board[i][j] == 'Y':
                end = (j, i)
    visited[start[0]][start[1]] = 1
    dfs(start[0], start[1], 0, K, (0, -1))
    if answer == 1e9:
        answer = -1
    print(f'#{test_case} {answer}')
