n,v = eval(input())
c, w = eval(input())

dp = [0 for _ in range(v+1)]
for _ in range(n):
    for j in range(v,c-1,-1):
        dp[j] = max(dp[j],dp[j-c]+w)
print(dp)