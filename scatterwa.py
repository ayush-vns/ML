import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the CSV data

df = pd.read_csv("scatterda.csv")

# Extract values for the scatter plots
x = df['random1'].values  # Values from column 'random1'

y = df['random2'].values  # Values from column 'random2'

# Generate two additional sets of random data
z = df['random3'].values  # Values from column 'random3'
w = df['random4'].values  # Generate 100 random values from a normal distribution with mean -1 and standard deviation 0.5

# Create a new figure and Axes object
fig, ax = plt.subplots()

# Plot the data as a scatter plot with blue circles as markers
ax.scatter(x, y, color='blue', marker='o', label='Set 1')
ax.scatter(z, w, color='green', marker='s', label='Set 2')
ax.scatter(np.random.normal(-2, 1, 100), np.random.normal(3, 1, 100), color='red', marker='^', label='Set 3')

# Set the title, x-axis label, and y-axis label
ax.set_title('Scatter Plot Example')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add a trend line to the plot using the np.polyfit() function
z1 = np.polyfit(x, y, 1)  # Calculate the coefficients for a linear trend line for Set 1
z2 = np.polyfit(z, w, 1)  # Calculate the coefficients for a linear trend line for Set 2
p1 = np.poly1d(z1)  # Create a polynomial function based on the coefficients for Set 1
p2 = np.poly1d(z2)  # Create a polynomial function based on the coefficients for Set 2
ax.plot(x, p1(x), color='red', linestyle='--', linewidth=2, label='Trend Line (Set 1)')  # Add the trend line for Set 1 to the plot
ax.plot(z, p2(z), color='black', linestyle='--', linewidth=2, label='Trend Line (Set 2)')  # Add the trend line for Set 2 to the plot

# Add a legend to the plot
ax.legend(loc='upper left')

# Customize the spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# Set the limits and tick marks for the x-axis and y-axis
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
ax.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])

# Display the plot
plt.show()