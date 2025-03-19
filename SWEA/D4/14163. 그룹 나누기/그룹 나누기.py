def union(parents, a, b):
    rootA = find(parents, a)
    rootB = find(parents, b)
    if rootA > rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB


def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    parents = [i for i in range(N + 1)]

    input_group = list(map(int, input().split()))
    for i in range(M):
        if find(parents, input_group[i*2]) != find(parents, input_group[i*2+1]):
            union(parents, input_group[i*2], input_group[i*2+1])
    for i in range(1, N + 1):
        parents[i] = find(parents, i)
    answer = len(set(parents[1:]))
    print(f'#{test_case} {answer}')
