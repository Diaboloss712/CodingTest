def dfs(mask, row):
    max_chance = 1e-50
    if row == N:
        return 1
    if dp[mask]:
        return dp[mask]
    for i in range(N):
        if not (mask & 1 << i):
            chance = board[row][i]
            max_chance = max(max_chance, chance * 0.01 * dfs((mask | 1 << i), row+1))
    dp[mask] = max_chance
    return max_chance


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (1 << N)
    answer = dfs(0, 0)
    print(f'#{test_case} {round(answer*100,6):6f}')
