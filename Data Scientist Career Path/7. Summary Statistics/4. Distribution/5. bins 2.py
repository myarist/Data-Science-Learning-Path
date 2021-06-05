# Import packages
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

# Count the values in each bin 
days_old_012 = 4
days_old_345 = 2
days_old_678 = 4

# Printing the values
print("Between 0 and 2 days: " + str(days_old_012))
print("Between 3 and 5 days: " + str(days_old_345))
print("Between 6 and 8 days: " + str(days_old_678))