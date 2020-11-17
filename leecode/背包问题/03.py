V, N = eval(input())
W, P = eval(input())

# V, N = 5, 4
# P, W = [1, 2, 3, 4], [1, 2, 3, 4]

d = [[0 for _ in range(N)] for __ in range(V + 1)]
'''
物品可重复放
d[row][col] = max(d[row - W[col]]) + P[col]  
状态转移方程，对于第row行表示此刻背包容积为row，放入第col个物体。
等于减去这个物体的重量后的第row-w[col]行的最大值。
'''
for row in range(V + 1):
    for col in range(N):
        if W[col] <= row:
            d[row][col] = max(d[row - W[col]]) + P[col]  # 状态转移方程，对于第
print(d)
