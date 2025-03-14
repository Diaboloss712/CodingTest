from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    global mini_board
    global q
    while q:
        x, y = q.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if mini_board[ny][nx] > mini_board[y][x] + 1:
                mini_board[ny][nx] = mini_board[y][x] + 1
                q.append((nx, ny))


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    q = deque()
    N, M = list(map(int, input().split()))
    mini_board = [[10000000] * M for _ in range(N)]
    board = [list(map(str, input())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'W':
                mini_board[i][j] = 0
                q.append((j, i))
    bfs()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'L':
                answer += mini_board[i][j]
    print(f'#{test_case} {answer}')
