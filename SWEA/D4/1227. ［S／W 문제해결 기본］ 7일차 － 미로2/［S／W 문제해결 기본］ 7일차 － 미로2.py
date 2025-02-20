dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(start):
    global board
    global answer
    visited = [[0] * 100 for _ in range(100)]
    queue = [start]
    while queue:
        cur_pos = queue.pop()
        cur_x = cur_pos[0]
        cur_y = cur_pos[1]
        for direction in range(4):
            nx = cur_x + dx[direction]
            ny = cur_y + dy[direction]
            if nx >= 100 or ny >= 100 or nx < 0 or ny < 0:
                continue
            if visited[ny][nx]:
                continue
            if board[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append([nx, ny])
            elif board[ny][nx] == 3:
                answer = 1
                return


for test_case in range(1, 11):
    T = int(input())
    answer = 0
    board = [[0] * 100 for _ in range(100)]
    for i in range(100):
        board[i] = list(map(int, input()))
    for i in range(100):
        for j in range(100):
            if board[i][j] == 2:
                start_x = j
                start_y = i
    bfs([start_x, start_y])
    print(f'#{test_case} {answer}')