def solution(info, n, m):
    answer = -1
    length = len(info)
    dp = [set() for _ in range(length)]

    if info[0][0] < n:
        dp[0].add((info[0][0], 0))
    if info[0][1] < m:
        dp[0].add((0, info[0][1]))
    for i in range(1, length):
        for data in dp[i - 1]:
            A_clue = data[0] + info[i][0], data[1]
            B_clue = data[0], data[1] + info[i][1]
            if A_clue[0] < n:
                dp[i].add(A_clue)
            if B_clue[1] < m:
                dp[i].add(B_clue)
    if dp[length - 1]:
        answer = min(dp[length - 1], key=lambda x: x[0])[0]
    return answer