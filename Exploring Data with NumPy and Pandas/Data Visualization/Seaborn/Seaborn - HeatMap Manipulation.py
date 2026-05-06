import seaborn as sns
import matplotlib as plt

# Heatmap
correlation_matrix = tips.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
