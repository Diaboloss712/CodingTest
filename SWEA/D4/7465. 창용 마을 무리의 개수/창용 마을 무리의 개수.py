def union(parents, a, b):
    rootA = find(parents, a)
    rootB = find(parents, b)
    if rootA > rootB:
        parents[rootB] = rootA
        for i in range(1, len(parents)):
            if find(parents, i) == rootA:
                parents[i] = rootA
            elif find(parents, i) == rootB:
                parents[i] = rootA
    else:
        parents[rootA] = rootB
        for i in range(1, len(parents)):
            if find(parents, i) == rootB:
                parents[i] = rootB
            elif find(parents, i) == rootA:
                parents[i] = rootB

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]

    for i in range(M):
        a, b = list(map(int, input().split()))
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
    answer = len(set(parents))
    print(f'#{test_case} {answer-1}')