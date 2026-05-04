import pandas as pd

# Creating a DataFrame from raw data
data = {
        "first_name": ["Jason", "Molly", "Tina", "Jake", "Amy"],
        "last_name": ["Miller", "Jacobson", ".", "Milner", "Cooze"],
        "age": [42, 52, 36, 24, 73],
        "preTestScore": [4, 24, 31, ".", "."],
        "postTestScore": ["25,000", "94,000", 57, 62, 70]
}

df = pd.DataFrame(data)
print("DataFrame created:")
print(df)

# Saving the DataFrame to a CSV file
df.to_csv("example.csv", index=False)
print("DataFrame saved as 'example.csv'.")

# Reading the CSV file
df_read = pd.read_csv("example.csv")
print("Data read from 'example.csv':")
print(df_read)

# Reading CSV without column headers
df_no_header = pd.read_csv("example.csv", header=None)
print("Data read without column headers:")
print(df_no_header)

# Reading CSV and setting custom index column
df_custom_index = pd.read_csv("example.csv", index_col=["first_name", "last_name"])
print("DataFrame with custom index (First Name, Last Name):")
print(df_custom_index)

# Reading the first 3 rows of the DataFrame
df_first_3_rows = pd.read_csv("example.csv").head(3)
print("First 3 rows of the DataFrame:")
print(df_first_3_rows)

# Removing commas from 'postTestScore' and converting to numeric
df["postTestScore"] = df["postTestScore"].replace({",": ""}, regex=True).astype(float)
print("DataFrame after cleaning postTestScore' column:")
print(df)
