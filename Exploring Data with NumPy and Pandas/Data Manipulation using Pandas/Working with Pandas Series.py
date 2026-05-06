import pandas as pd
import numpy as np

# Creating a Pandas Series from a list
x = [13, -5, 7, 19]
series_from_list = pd.Series(x)
print("Series from list:")
print(series_from_list)

# Creating a Series from a NumPy array and specifying custom index
array = np.array([23, 3.0, 7, 11])
series_from_array = pd.Series(array, index=["a", "b", "c", "d"])
print("Series from NumPy. array with custom index:")
print(series_from_array)

# Accessing values and index of the series
values = series_from_array.values
index = series_from_array.index
print("Values:", values)
print("Index:", index)

# Accessing individual elements using index
print("Accessing element at index 'a':", series_from_array['a'])
print("Accessing element at index 'b':", series_from_array['b'])

# Modifying elements in the Series
series_from_array["c"] = 10
print("Series after modification:")
print(series_from_array)

# Creating a Pandas Series with raw data
raw_data = ["Amit", "Bob", "Kate", "A", "b", np.nan, "Car", "dog", "cat"]
series_strings = pd.Series(raw_data)
print("Original Series:")
print(series_strings)

# Converting all elements to lowercase
print("Lowercase elements:")
print(series_strings.str.lower())

# Converting all elemets to uppercase
print("Uppercase elements:")
print(series_strings.str.upper())

# Finding the length of all elements
print("Length of each element:")
print(series_strings.str.len())

# Creating a Pandas Series with names containing spaces
names = [" Arya", "John", " jack", "Sam"]
series_names = pd.Series(names)
print("Original Series:")
print(series_names)

# Stripping spaces from both sides
print("Names after stripping spaces from both sides:")
print(series_names.str.strip())

# Removing spaces from the left side only
print("Names after removing spaces from the left side:")
print(series_names.str.lstrip())

# Removing spaces from the right side only
print("Names after removing spaces from the right side:")
print(series_names.str.rstrip())
