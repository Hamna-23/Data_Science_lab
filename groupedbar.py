import matplotlib.pyplot as plt
import numpy as np

groups = ['A', 'B', 'C', 'D', 'E']  # group names on x-axis
men_scores = [22, 30, 35, 36, 26]
women_scores = [25, 32, 30, 35, 29]

n_groups = len(groups)


index = np.arange(n_groups)


bar_width = 0.35


fig, ax = plt.subplots()

# Bars for men and women side by side
bars1 = ax.bar(index, men_scores, bar_width, label='Men', color='blue')
bars2 = ax.bar(index + bar_width, women_scores, bar_width, label='Women', color='pink')

# Labels and title
ax.set_xlabel('Groups')
ax.set_ylabel('Scores')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(groups)

# Add legend
ax.legend()

# Show the plot
plt.show()
