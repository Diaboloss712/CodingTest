from collections import deque

def solution(n, edge):
    answer = 0
    edge.sort()
    distance = [0] * (n+1)
    queue = deque()
    board = [[] * (n+1) for _ in range(n+1)]
    
    for route in edge:
        board[route[0]].append(route[1])
        board[route[1]].append(route[0])
    queue.append(1)
    distance[1]=1
    
    while queue:
        current = queue.popleft()
        for node in board[current]:
            if distance[node] == 0:
                queue.append(node)
                distance[node] = distance[current] + 1
    max_distance = max(distance)
    for dist in distance:
        if dist == max_distance:
            answer += 1
    return answer