# Histogram and KDE plot - shows distibution of a single continuous variable
sns.histplot(tips['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.show()

# Box plot - Compare distributions across categories
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title("Box Plot of Total Bill by Day")
plt.show()

# Pair plot - Visualize pairwise relationships in a dataset
sns.pairplot(tips, hue='day')
plt.show()

# Bar plot - Show the distribution of a categorical variables:
sns.barplot(x='day', y='total_bill', data=tips)
plt.title("Average Total Bill by Day")
plt.show()

# Set style
sns.set_style('whitegrid')
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title("Scatter Plot with Whitegrid Style")
plt.show()

# Custom colors
sns.scatterplot(x='total_bill', y='tip', data=tips, palette='coolwarm')
plt.title("Scatter Plot with Custom Colors")
plt.show()
