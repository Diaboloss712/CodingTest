def solution(n, w, num):
    answer = 0
    height = n//w
    board = [[0] * w for _ in range(height+1)]
    for i in range(height + 1):
        for j in range(w):
            if (i+1) % 2 == 0:
                board[i][j] = (i+1) * w - j
            else:
                board[i][j] = i * w + (j+1)
            if board[i][j] == num:
                x = j
                y = i
    for i in range(height+1):
        if board[i][x] >= num and board[i][x] <= n:
            answer += 1
    return answer