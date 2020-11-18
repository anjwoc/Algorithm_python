import sys
input = sys.stdin.readline

# DP[i][j]: i,j에 도착했을 때 최대값
# DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + DP[i][j]

n = int(input())
A = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        A[i][j] = tmp[j-1]


for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + A[i][j]

print(max(dp[n]))
