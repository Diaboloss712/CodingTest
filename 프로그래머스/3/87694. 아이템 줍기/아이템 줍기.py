dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer, visited, board
    answer = float('inf')
    board = [[0] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]

    for cur_rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, cur_rec)
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if x1 < j < x2 and y1 < i < y2:
                    board[i][j] = 2
                elif board[i][j] != 2:
                    board[i][j] = 1

    char_pos = (characterX * 2, characterY * 2)
    item_pos = (itemX * 2, itemY * 2)
    visited[char_pos[1]][char_pos[0]] = 1
    dfs(char_pos[0], char_pos[1], item_pos[0], item_pos[1], 0)

    return answer // 2

def dfs(x, y, item_x, item_y, depth):
    global answer

    if depth >= answer:
        return

    if (x, y) == (item_x, item_y):
        answer = min(answer, depth)
        return

    for direction in range(4):
        nx, ny = x + dx[direction], y + dy[direction]

        if 0 <= nx < 102 and 0 <= ny < 102 and board[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs(nx, ny, item_x, item_y, depth + 1)
            visited[ny][nx] = 0