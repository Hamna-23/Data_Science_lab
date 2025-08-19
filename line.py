import matplotlib.pyplot as plt

# Coordinates
x = [1, 2, 6, 18]
y = [3, 10, 12, 20]

plt.plot(x, y, color='blue', linestyle=':', marker='*', markerfacecolor='red', markeredgecolor='blue')

# Add labels and title
plt.title("Dotted Line with Red Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Annotate each point
for i in range(len(x)):
    plt.text(x[i] + 0.5, y[i], f"({x[i]}, {y[i]})", fontsize=9)

# Show plot
plt.show()
