# Read diabetes data from first file
df1 = pd.read_csv("/content/diabetes_data1.csv", index_col="PatientID")
df1.head()

# Print the shape of the DataFrame
df1.shape

# Read data from second file which contains additional rows
df2 = pd.read_csv('diabetes_data1_newRows.csv', index_col="PatientID")
print(df2.shape)

df2.head()

data1 = pd.concat([df1, df2])
print(data1.shape)

# Read data from third CSV file which contains additional columns
df3 = pd.read_csv('/content/diabetes_data2.csv', index_col="PatientID")
print(df3.shape)

data2 = pd.concat([data1,df3], axis=1)
print(data2.shape)

# Left join 
df_left=pd.merge(data1, df3, on="PatientID", how="left")
print(df_left.shape)

# Right join 
df_right=pd.merge(data1, df3, on="PatientID", how="right")
print(df_right.shape)

# Outer join
df_outer = pd.merge(data1, df3, on="PatientID", how="outer")
print(df_outer.shape)

# Inner join
df_inner = pd.merge(data1, df3, on="PatientID", how="inner")
print(df_inner.shape)
