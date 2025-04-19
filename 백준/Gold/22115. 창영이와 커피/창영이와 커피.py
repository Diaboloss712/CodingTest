N, K = list(map(int,input().split()))
C = [0] + list(map(int,input().split()))

dp = [[1000001] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 0
for i in range(1, N+1):
    for j in range(1, K+1):
        if j < C[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-C[i]] + 1)

if dp[N][K] == 1000001:
    print(-1)
else:
    print(dp[N][K])