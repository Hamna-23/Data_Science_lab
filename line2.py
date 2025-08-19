import matplotlib.pyplot as plt


x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]


x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 6, 8, 10]


x3 = [1, 2, 3, 4, 5]
y3 = [3, 5, 7, 9, 12]

#
plt.plot(x1, y1, label='Line 1', marker='o')
plt.plot(x2, y2, label='Line 2', marker='*')
plt.plot(x3, y3, label='Line 3', marker='+')


plt.title("Multiple Lines on Same Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.legend()


plt.grid(True)

plt.show()
