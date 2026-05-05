# Importing libraries
import numpy as np
import matplotlib as plt
import random

%matplotlib inline

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creating a figure and an axis
fig, ax = plt.subplots()

# Plotting
ax.plot(x, y, label='sin(x)', color='blue')
ax.set_title("Sine function")
ax.set_xlabel("X values")
ax.set_ylabel("sin(x)")
ax.legend()
ax.grid(True)

# Displaying the plot
plt.show()

# Scatter Plot

# Sample data
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)

# Creating a figure and an axis
fig, ax = plt.subplots()

# Creating a scatter plot
ax.scatter(x, y, color='red')
ax.set_title("Random Scatter Plot")
ax.set_xlabel("X values")
ax.set_ylabel("Y values")
ax.grid(True)

# Displaying the plot
plt.show()

# Bar Chart

# Sample data
categories = ["A", "B", "C", "D"]
values = [3, 7, 2, 5]

# Creating a figure and an axis
fig, ax = plt.subplots()

# Creating a bar plot
ax.bar(categories, values, color='purple')
ax.set_title("Bar Plot Example")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")

# Displaying the plot
plt.show()
