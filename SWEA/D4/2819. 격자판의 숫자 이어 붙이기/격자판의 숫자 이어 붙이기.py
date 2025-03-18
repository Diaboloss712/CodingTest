dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(start, depth, string):
    string = string+(str(board[start[1]][start[0]]))
    if depth == 7:
        answer.add(string)
        return
    for direction in range(4):
        nx = start[0] + dx[direction]
        ny = start[1] + dy[direction]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        dfs((nx, ny), depth + 1, string)


T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            dfs((j, i), 1, '')
    print(f'#{test_case} {len(answer)}')