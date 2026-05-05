# Import the required libraries
import pandas as pd
import numpy as np

# Read sample of diabetes data from a CSV file
df = pd.read_csv("diabetes_sample.csv")

# Check if there are any null values in the data
print(df.isnull())

# Check for null values in column Insulin
print(df.Insulin.isnull())

# Fill the rows containing null values in Insulin column with the mean value
df.Insulin = df.Insulin.fillna(df.Insulin.mean())
# Observe that the null value is filled using the mean

# Check for dublicate rows
df.dublicated()

# Check if any patient has a dublicate entry using PatientID column
df.dublicated(["PatientID"])
# Observe that one more entry is returned as True in this case
