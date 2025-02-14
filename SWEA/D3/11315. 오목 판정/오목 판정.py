dx = [1, 1, 1, 0]
dy = [-1, 1, 0, 1]

def dfs(x, y):
    global answer
    global board
    for direction in range(4):
        count = 1
        while 1:
            nx = x + dx[direction]*count
            ny = y + dy[direction]*count
            if 0 <= nx < N and 0 <= ny < N:
                if board[ny][nx] == 1:
                    count += 1
                else:
                    break
                if count==5:
                    answer = "YES"
                    return
            else:
                break
    return



T = int(input())
for test_case in range(1, T+1):
    answer = "NO"
    N = int(input())
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        string = input()
        for j in range(N):
            if string[j] == 'o':
                board[i][j] = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                dfs(j, i)
    print(f'#{test_case} {answer}')