import pandas as pd

# Loading data from a CSV file into a Pandas DataFrame
data = pd.read_csv("data.csv")
print(data.head()) # Displaying the first 5 rows of the data

# Example: Creating a Pandas Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# Example: Creating a DataFrame
data = {"Name": ["John", "Jane", "Doe"],
        "Age": [25, 28, 22],
        "Occupation": ["Engineer", "Doctor", "Artist"]}

df = pd.DataFrame(data)
print(df)

# Viewing the first 5 rows
print(pd.head())

# Viewing the last 5 rows
print(df.tail())
