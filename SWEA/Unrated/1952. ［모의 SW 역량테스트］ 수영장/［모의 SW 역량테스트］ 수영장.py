T = int(input())
for test_case in range(1, T+1):
    plan = []
    day, month, three_month, year = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] * 12
    answer = 0
    dp[0] = min(plan[0] * day, month)
    dp[1] = dp[0] + min(plan[1] * day, month)
    dp[2] = min(dp[1] + min(plan[2] * day, month), three_month)
    for i in range(3, 12):
        dp[i] = min(dp[i - 1] + min(plan[i] * day, month), dp[i-3] + three_month)
        if i >= 11:
            dp[i] = min(min(dp[i - 1] + min(plan[i] * day, month), dp[i-3] + three_month), year)
    print(f'#{test_case} {dp[11]}')
