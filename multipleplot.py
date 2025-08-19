import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 rows, 2 columns

axs[0, 0].plot(x, np.sin(x), color='blue')
axs[0, 0].set_title("Sine Wave")


axs[0, 1].plot(x, np.cos(x), color='red')
axs[0, 1].set_title("Cosine Wave")


axs[1, 0].plot(x, np.tan(x), color='green')
axs[1, 0].set_ylim(-10, 10)  # limit y-axis
axs[1, 0].set_title("Tangent Wave")


axs[1, 1].plot(x, np.exp(-x), color='purple')
axs[1, 1].set_title("Exponential Decay")


plt.tight_layout()


plt.show()
