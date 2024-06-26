import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("barwa.csv")


categories = df['name'].values

values1 = df['value1'].values

values2 = df['value2'].values

# Create a bar plot with customizations
bar_width = 0.35
plt.bar(categories, values1, color='green', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width)
plt.bar(categories, values2, color='aqua', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width, bottom=values1)

# Add error bars
errors = [2, 1, 3, 2]
plt.errorbar(categories, values1, yerr=errors, fmt='none', capsize=5)
plt.errorbar(categories, values2, yerr=errors, fmt='none', capsize=5)

# Add annotations
for i, (v1, v2) in enumerate(zip(values1, values2)):
    plt.text(i-bar_width/2, v1+1, str(v1), ha='center', fontweight='bold')
    plt.text(i+bar_width/2, v2+1, str(v2), ha='center', fontweight='bold')

# Add a legend
plt.legend(['CR 1', 'Cr 2', 'Error'])

# Add titles and labels
plt.title('Fruit Sales')
plt.xlabel('Fruit')
plt.ylabel('Number of Sales')

# Display the plot
plt.show()