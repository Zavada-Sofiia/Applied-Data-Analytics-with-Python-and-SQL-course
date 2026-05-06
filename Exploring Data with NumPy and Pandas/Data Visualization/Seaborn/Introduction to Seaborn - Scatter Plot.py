import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

# Load a sample dataset
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
tips.head()

# Scatter Plot - used to display relationships between two continuous variables
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='day')
plt.title("Scatter Plot of Tip vs Total Bill")
plt.show()
