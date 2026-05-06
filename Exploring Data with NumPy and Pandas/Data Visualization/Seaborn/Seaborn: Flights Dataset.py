import seaborn as sns
import matplotlib as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('content/flights.csv')
df.read()

# Histogram and KDE plot of passenger counts
plt.figure(figsize=(12, 6))
sns.histplot(df["passengers"], kde=True, bins=30, color='skyblue')
plt.title("Histogram and KDE Plot of Passenger Counts")
plt.show()
