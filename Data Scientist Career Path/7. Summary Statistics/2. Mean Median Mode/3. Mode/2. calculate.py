import numpy as np

# Set first_ten_authors equal to their ages
first_ten_authors = np.array([29, 49, 42, 43, 32, 38, 37, 41, 27, 27])

# Save the mode value to mode_age
mode_age = 27

# Save the count of authors with the mode age
mode_count = 2

# Print the sorted array and median value
print("The ages of the first ten authors is: " + str(first_ten_authors))
print("The mode of the first ten authors is: " + str(mode_age))
print("The number of authors who were " + str(mode_age) + " when their book was published is " + str(mode_count))