def solution(n, costs):
    answer = 0
    parents = [i for i in range(n+1)]
    costs.sort(key=lambda x : x[2])
    for route in costs:
        if find(parents, route[0]) == find(parents, route[1]):
            continue
        else:
            union(parents, route[0], route[1])
            answer += route[2]
    return answer


def union(parents, x, y):
    num1 = find(parents, x)
    num2 = find(parents, y)
    if num1 > num2:
        parents[num1] = num2
    else:
        parents[num2] = num1

def find(parents, x):
    while parents[x] != x:
        x = parents[x]
    return x