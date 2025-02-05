import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 8)
ax.set_ylim(0, 3)
ax.axis('off')

# Add rectangles for each step
steps = ['Input', 'Preprocessing', 'Prediction', 'Output']
positions = [(0.5, 1), (2.5, 1), (4.5, 1), (6.5, 1)]
for step, (x, y) in zip(steps, positions):
    rect = Rectangle((x, y), 1.5, 1, edgecolor='black', facecolor='lightblue', lw=2)
    ax.add_patch(rect)
    ax.text(x + 0.75, y + 0.5, step, ha='center', va='center', fontsize=12, weight='bold')

# Add arrows between the steps
for i in range(len(positions) - 1):
    start_x, start_y = positions[i][0] + 1.5, positions[i][1] + 0.5
    end_x, end_y = positions[i + 1][0], positions[i + 1][1] + 0.5
    arrow = FancyArrow(start_x, start_y, end_x - start_x - 0.1, 0, width=0.05, color='black')
    ax.add_patch(arrow)

# Save or show the figure
plt.tight_layout()
plt.savefig("flowchart.png", dpi=300)
plt.show()
