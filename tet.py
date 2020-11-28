a = 2
b = a
[b := a * b for _ in range(3)]
print(b)
