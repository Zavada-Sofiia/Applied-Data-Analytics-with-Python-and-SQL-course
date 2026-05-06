
# Box plot of passenger by month
plt.figure(figsize=(12, 6))
sns.boxplot(x='month', y='passengers', data=df, palette='Set2')
plt.title("Box Plot of Passengers by Month")
plt.xsticks(rotation=45)
plt.show()

# Example Pair Plot (assuming additional numerical columns exist)
sns.pairplot(df, hue='month', palette='viridis')
plt.show()

# Pivot table for heatmap
pivot_table = df.pivot(index="month", columns="year", values="passengers")

# Heatmap of passengers
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap="YlGnBu", annot=True, fmt="d")
plt.title("Heatmap of Passengers by Month and Year")
plt.show()

# Set a custom theme
sns.set_theme(style="darkgrid")

# Custom color palette
sns.set_palette('colorblind')

# Example Box Plot with custom settings
plt.figure(figsize=(12, 6))
sns.boxplot(x="month", y="passengers", data=df)
plt.title("Box Plot with Custom Theme and Palette")
plt.xticks(rotation=45)
plt.show()
