import heapq
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dijkstra():
    q = []
    distance[0][0] = 0
    start_x = 0
    start_y = 0
    heapq.heappush(q, (0, start_x, start_y))
    while q:
        dist, x, y = heapq.heappop(q)
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if dist + board[ny][nx] < distance[ny][nx]:
                distance[ny][nx] = dist + board[ny][nx]
                if nx == N-1 and ny == N-1:
                    return
                heapq.heappush(q, (dist + board[ny][nx], nx, ny))


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    global board
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        board[i] = list(map(int, input()))
    distance = [[INF] * (N + 1) for _ in range(N + 1)]
    dijkstra()
    print(f'#{test_case} {distance[N-1][N-1]}')
