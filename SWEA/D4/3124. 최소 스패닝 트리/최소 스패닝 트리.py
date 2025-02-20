def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents, a, b):
    rootA = find(parents, a)
    rootB = find(parents, b)

    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB


T = int(input())
for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))
    edges = []
    answer = 0
    parents = [0] * (V+1)
    parents = [i for i in range(V+1)]
    for i in range(E):
        edges.append(list(map(int, input().split())))
    edges.sort(key = lambda x:x[2])
    for edge in edges:
        if find(parents, edge[0]) == find(parents, edge[1]):
            continue
        else:
            answer += edge[2]
            union(parents, edge[0], edge[1])
    print(f'#{test_case} {answer}')