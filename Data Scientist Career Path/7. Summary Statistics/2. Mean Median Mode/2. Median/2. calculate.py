import numpy as np

# Array of the first five author ages
five_author_ages = np.array([29, 49, 42, 43, 32])

# Fill in the empty array with the values sorted
sorted_author_ages = np.array([29, 32, 42, 43, 49])

# Save the median value to median_value
median_age = 42

# Print the sorted array and median value
print("The sorted array is: " + str(sorted_author_ages))
print("The median of the array is: " + str(median_age))