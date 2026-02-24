def solution(n, s, a, b, fares):
    INF = 10**9
    answer = INF
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for start, end, cost in fares:
        dist[start-1][end-1] = cost
        dist[end-1][start-1] = cost
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    for k in range(n):
        cost = dist[s-1][k] + dist[k][a-1] + dist[k][b-1]
        answer = min(answer, cost)
    return answer