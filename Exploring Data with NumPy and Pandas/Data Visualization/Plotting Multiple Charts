# Subplots

# Creating subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Line plot
axs[0, 0].plot(x, y, label='sin(x)')
axs[0, 0].set_title("Sine function")
axs[0, 0].legend()

# Scatter Plot
axs[0, 1].scatter(x, y, color='red')
axs[0, 1].set_title("Random Scatter Plot")

# Bar Plot
axs[1, 0].bar(categories, values, color='purple')
axs[1, 0].set_title("Bar Plot Example")

# Histogram
axs[1, 1].hist(data, bins=30, color='green', alpha=0.7)
axs[1, 1].set_title("Histogram of Random Data")

plt.tight_layout() # Adjusts layout for better fit
plt(show)

# Creating a basic lineplot
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

# Saving figure
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
