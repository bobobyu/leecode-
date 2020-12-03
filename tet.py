n = 150000
cout_ = 1
sol = [2]
for i in range(3, n, 2):
    flg = 1
    for j in sol:
        if not i % j:
            flg = 0
            break
    if flg:
        cout_ += 1
        sol.append(i)
print(cout_, sol)