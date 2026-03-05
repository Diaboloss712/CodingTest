def solution(clothes):
    d = {}
    for _, kind in clothes:
        d[kind] = d.get(kind, 1) + 1

    cnt = 1
    for v in d.values():
        cnt *= v
    return cnt - 1