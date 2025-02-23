from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    queue = deque()
    queue.append((0,0))
    x_arr = [-1,1,0,0]
    y_arr = [0,0,1,-1]
    
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            new_x = x + x_arr[i]
            new_y = y + y_arr[i]
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n :
                continue
            elif maps[new_x][new_y] == 1 :
                maps[new_x][new_y] += maps[x][y]
                queue.append([new_x, new_y])
     
    return -1 if maps[m-1][n-1] < 2 else maps[m-1][n-1]
