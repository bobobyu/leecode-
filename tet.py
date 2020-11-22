import matplotlib.pyplot as plt
a = [13, -3, -25, 20, -3, -16, -23, 18,
     20, -7, 12, -5, -22, 15, -4, 7]
sum = 0
x = []
for i in a[:8][::-1]:

     sum += i
     x.append(sum)

plt.plot(x, marker='o')
plt.show()