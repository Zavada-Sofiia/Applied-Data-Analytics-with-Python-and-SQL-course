import numpy as np
import random

movie_id = np.arrange(1301, 2301)
print(movie_id[:10]) # Shows the first 10 movie IDs
print(movie_id.size) # Size of the array

user_id = []
for i in range(20201, 20301):
    user_id.append(i)
user_id = np.array(user_id)
print(user_id.size) # Checking the number of elements in the array

arr = np.array([2, 3, 7]) # Single-Dimensional Array
print(arr)

arr = np.array([[10, 20, 30], [40, 50, 60]]) # Multi-Dimensional Array
print(arr)
print(type(arr))

arr = np.empty([2, 2], dtype=complex) # Empty array with complex type
print(arr)

X = np.full((2, 3), 5) # Array filled with the value 5
print(X)

arr = np.zeros([2, 3]) # Array filled with zeros
print(arr)

arr = np.ones([3, 5]) # Array filled with ones
print(arr)

movie_matrix = []
for user in range(100):
    movies_rated_by_me = np.full(1000, -1)
    num_movies_rated = random.randint(0, 999)
    movies_that_i_will_rate = random.sample(range(0, 1000), num_movies_rated)
    for index in movies_that_i_will_rate:
        movies_rated_by_me[index] = random.randint(0, 10)
    movie_matrix.append(movies_rated_by_me)

movie_matrix = np.array(movie_matrix)
print(movie_matrix)
print("Shape of the array:", movie_matrix.shape)

expert_matrix = []
for user in range(10):
    movies_rated_by_me = np.full(1000, -1)
    num_movies_rated = random.randint(0, 999)
    movies_that_i_will_rate = random.sample(range(0, 1000), num_movies_rated)
    for index in movies_that_i_will_rate:
        movies_rated_by_me[index] = random.randint(0, 10)
    expert_matrix.append(movies_rated_by_me)
expert_matrix = np.array(expert_matrix)

# Stacking arrays vertically
movie_matrix = np.vstack([movie_matrix, expert_matrix])

# Adding 50 new moves
new_movies_matrix = []
for user in range(110):
    movies_rated_by_me = np.full(50, -1)
    num_movies_rated = random.randint(0, 49)
    movies_that_i_will_rate = random.sample(range(0, 50), num_movies_rated)
    for index in movies_that_i_will_rate:
        movies_rated_by_me[index] = random.randint(0, 10)
    new_movies_matrix.append(movies_rated_by_me)
new_movies_matrix = np.array(new_movies_matrix)

movie_matrix = np.hstack([movie_matrix, new_movies_matrix])
print(movie_matrix.shape) # 110 users and 1050 movies

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(arr)) # Minimum
print(np.amax(arr, axis=1)) # Max along axis 1
print(np.mean()) # Mean
print(np.std()) # Standart Deviation
print(np.median(arr)) # Median
