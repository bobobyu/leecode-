epochs: int = int(input())
res = []
for i in range(epochs):
    data_: list = [int(i) for i in input().split(' ')]
    a = data_[1]
    b = data_[2]
    max_k: int = min(a, b)
    n = data_[0]
    while max_k > 0 and a // max_k * b // max_k <= n:
        max_k -= 1
    res.append(max_k)
[print(i) for i in res]
