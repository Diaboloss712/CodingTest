def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    m = len(onboard)
    n = 51
    check = 1
    if temperature < t1:
        check = 0
    dp = [[1000001] * (n+1) for _ in range(m)]
    dp[0][temperature] = 0
    for i in range(1, m):
        for j in range(n):
            if not check:
                if temperature < j < 50:
                    dp[i][j] = min(dp[i - 1][j + 1], dp[i - 1][j] + b, dp[i - 1][j - 1] + a)
                elif j == temperature:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
                elif j == 50:
                    dp[i][j] = min(dp[i - 1][j - 1] + a, dp[i - 1][j] + b)
                else:
                    continue

            else:
                if 0 < j < temperature:
                    dp[i][j] = min(dp[i - 1][j + 1] + a, dp[i - 1][j] + b, dp[i - 1][j - 1])
                elif j == temperature:
                    dp[i][j] = min(dp[i - 1][j + 1], dp[i - 1][j], dp[i - 1][j - 1])
                elif j == 0:
                    dp[i][j] = min(dp[i - 1][j] + b, dp[i - 1][j + 1] + a)
                else:
                    continue
            if onboard[i]:
                if t1 <= j <= t2:
                    continue
                else:
                    dp[i][j] = 1000001
    answer = 1000001
    for i in range(n):
        if answer > dp[m - 1][i]:
            answer = dp[m - 1][i]
    return answer