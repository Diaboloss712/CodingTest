dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(start, distance, start_data):
    global answer
    global start_here
    cur_x, cur_y = start
    for direction in range(4):
        nx = cur_x + dx[direction]
        ny = cur_y + dy[direction]
        if nx < 0 or ny < 0 or nx >= len(board[0]) or ny >= N:
            continue
        if visited[ny][nx]:
            continue
        if board[ny][nx] == board[cur_y][cur_x] + 1:
            dfs((nx, ny), distance+1, start_data)
    if distance > answer:
        answer = distance
        start_here = start_data
    elif distance == answer:
        if start_here > start_data:
            start_here = start_data


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    start_here = 10000
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * len(board[0]) for _ in range(N)]
    for i in range(N):
        for j in range(len(board[i])):
            dfs((j, i), 1, board[i][j])
    print(f'#{test_case} {start_here} {answer}')