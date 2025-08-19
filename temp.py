import matplotlib.pyplot as plt
temperature = [12, 14, 16, 18, 20, 22, 24]
sales = [100, 200, 250, 400, 300, 450, 500]

plt.figure(figsize=(8,5))
plt.plot(temperature, sales, marker='o', linestyle='-', color='blue')

plt.title("Sales vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
