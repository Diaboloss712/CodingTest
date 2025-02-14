def dfs(start, end):
    global graph
    global visited
    global V
    global answer
    if visited[start]:
        return
    visited[start] = 1
    for j in range(V):
        if graph[start][j] == 1 and not visited[j]:
            if j == end:
                answer = 1
                return
            dfs(j, end)
            visited[j] = 0
    return


for test_case in range(1, 11):
    answer = 0
    T, E = list(map(int, input().split()))
    V = 100
    route = list(map(int, input().split()))
    graph = [[0] * V for _ in range(V)]
    visited = [0] * V
    for i in range(E):
        graph[route[i*2]][route[i*2+1]] = 1
    dfs(0, 99)
    print(f'#{test_case} {answer}')