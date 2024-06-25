import matplotlib.pyplot as plt
import numpy as np
# Simple plots
# Generate some data for the plot
x = np.linspace(0, 10, 100)  # Create an array of 100 evenly spaced points between 0 and 10
y = np.sin(x)  # Calculate the sine of each x value

# Create a new figure and Axes object
fig, ax = plt.subplots()

# Plot the data as a line with red color, solid line style, and a linewidth of 2
ax.plot(x, y, color='red', linestyle='-', linewidth=2)

# Set the title, x-axis label, and y-axis label
ax.set_title('Sine Wave')  # Set the title of the plot
ax.set_xlabel('X-axis')  # Set the label for the x-axis
ax.set_ylabel('Y-axis')  # Set the label for the y-axis

# Add gridlines to the plot
ax.grid(True, linestyle='--', color='gray', alpha=0.5)

# Customize the tick labels and locations
ax.set_xticks(np.linspace(0, 10, 11))  # Set the x-axis tick locations to be 11 evenly spaced values between 0 and 10
ax.set_xticklabels(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])  # Set the x-axis tick labels to be string values
ax.set_yticks(np.linspace(-1, 1, 11))  # Set the y-axis tick locations to be 11 evenly spaced values between -1 and 1
ax.tick_params(axis='both', labelsize=10)  # Set the font size of the tick labels to 10

# Add a legend to the plot
ax.legend(['Sine Wave'], loc='upper right')

# Customize the spines
ax.spines['top'].set_visible(False)  # Hide the top spine of the plot
ax.spines['right'].set_visible(False)  # Hide the right spine of the plot
ax.spines['bottom'].set_linewidth(1.5)  # Increase the width of the bottom spine to 1.5
ax.spines['left'].set_position(('outward', 10))  # Move the left spine outward by 10 points

# Display the plot
plt.savefig("ppp.png")
plt.show()

