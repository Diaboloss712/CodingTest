def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        if rootA > rootB:
            parents[rootA] = rootB
        else:
            parents[rootB] = rootA


def find(x):
    if x == parents[x]:
        return x
    return find(parents[x])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    parents = [i for i in range(N + 1)]
    answer = 0
    islands_x = input().split()
    islands_y = input().split()
    q = []
    E = float(input())

    for i in range(0, N):
        for j in range(i + 1, N):
            q.append([i + 1, j + 1, (abs(int(islands_x[i]) - int(islands_x[j])) ** 2 + abs(
                int(islands_y[i]) - int(islands_y[j])) ** 2) * E])
    q.sort(key=lambda x: x[2])

    for edge in q:
        x, y, cost = edge
        if find(x) == find(y):
            continue
        else:
            union(x, y)
            answer += cost
    answer = int(round(answer))
    print(f'#{test_case} {answer}')
