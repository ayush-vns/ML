import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("testing.csv")

x = df['rank'].values

y_sin =np.sin(x)
y_cos =np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y_sin, color='red', linestyle='-', linewidth=2, label='Sine')
ax.plot(x, y_cos, color='blue', linestyle='--', linewidth=2, label='cosine')

ax.set_title('Sine and Cosine Waves')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.grid(True, linestyle='--', color='gray', alpha=0.5)

ax.set_xticks(np.linspace(0, 10, 11))
ax.set_xticklabels(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
ax.set_yticks(np.linspace(-1, 1, 11))
ax.tick_params(axis='both', labelsize=10)

ax.legend(loc='upper right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_position(('outward', 10))

plt.show()