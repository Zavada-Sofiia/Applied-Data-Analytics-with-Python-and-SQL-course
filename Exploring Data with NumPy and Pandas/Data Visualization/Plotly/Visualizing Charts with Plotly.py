import pandas as pd
import plotly.express as px

data = {
        "Model": ["Model A", "Model B", "Model C", "Model D"],
        "Accuracy": [0.85, 0.90, 0.75, 0.95],
        "F1 Score": [0.83, 0.88, 0.70, 0.92],
        "Training Time (s)": [120, 150, 90, 200]
}

df.pd.DataFrame(data)
df.head()

# Scatter plot - Relationship between accuracy and F1 score
fig = px.scatter(df, 
                x='Accuracy', 
                y='F1 Score', 
                color='Model', 
                size='Training Time (s)', 
                hover_name='Model', 
                title='Accracy vs F1 Score',
                size_max=60)

# Show figure
fig.show()

