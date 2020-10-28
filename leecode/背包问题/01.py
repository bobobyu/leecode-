# V, N = eval(input())
# W, P = eval(input())

V, N = 4, 3

W, P = (1, 4, 3), (1500, 3000, 2000)

d = [[0 for j in range(N)] for i in range(V)]

'''
每个物品只能取一次
d[i][j] = max(d[max(i - 1, 0)][j] + P[j] + max(d[i - W[j]]))
d[max(0, i-1)][j]表示不放入这个物品，沿用V-1时的配置
P[j] + max(d[i - W[j][:max(0, j-1)]) 表示放入这个物品，沿用V-Wi时的最大配置

'''

for j in range(N):
    for i in range(V):
        if i >= W[j]:
            print(d[max(i - 1, 0)][j])
            print(P[j] + d[i - W[j]][max(0, j - 1)])
            d[i][j] = max(d[max(i - 1, 0)][j] , P[j] + d[i - W[j]] [max(0, j - 1)])
            print(d[i][j])

[print(i) for i in d]
