n = 8
a = [1, 2, 3, 4, 5, 6, 7, 8]

dp = [0 for _ in range(n)]

dp[0] = a[0]
sm = a[0]
for i in range(1, n):
    dp[i] = a[i] + min(0, dp[i-1])
    sm = min(sm, dp[i])

print(sm)