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

# Bar Chart - compare accuracies of different models
fig = px.bar(df, 
            x='Model', 
            y='Accuracy', 
            title='Model Accuracy Comparison', 
            color='Model', 
            text='Accuracy')

# Adding text on bars
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

# Pie chart - divide the total time taken by all the models .. Pie = SUM(the time taken by all the models)
fig = px.pie(df, 
            values='Training Time (s)', 
            names='Model', 
            title='Training Time Distribution by Model', 
            hover_data=['Accuracy', 'F1 Score'])

# Show figure
fig.show()

time_data = {
    "Epoch": [1, 2, 3, 4, 5],
    "Model A": [0.82, 0.85, 0.86, 0.87, 0.88],
    "Model B": [0.79, 0.82, 0.85, 0.87, 0.90]
}
time_data = pd.DataFrame(time_data)
time_data.head()

# Line chart
time_df_melted = time_df.melt(id_vars="Epoch", var_name="Model", value_name="Accuracy")

fig = px.line(time_df_melted, 
            x="Epoch", 
            y="Accuracy", 
            color="Model", 
            title="Model Accuracy Over Epochs")

# Show figure
fig.show()
