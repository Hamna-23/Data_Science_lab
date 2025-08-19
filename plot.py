import matplotlib.pyplot as plt
temp = [12, 14, 16, 18, 20, 22, 24]
celsius = [100, 200, 250, 400, 300, 450, 500]


plt.plot(temp, celsius, marker='o', color='green', linestyle='-')


plt.title("Temperature vs Celsius Plot")
plt.xlabel("Temperature (°C)"
           )
plt.ylabel("Celsius Value")


plt.grid(True)

plt.show()
