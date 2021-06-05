# Import packages
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

# Set the minimum and maximums of the array below
min_days_old = np.amin(days_old_bread)
max_days_old = np.amax(days_old_bread)

# Set the number of bins to 3
bins = 3

# Calculate the bin range
try:
	bin_range = (max_days_old - min_days_old + 1) / bins
	print("Bins: " + str(bins))
	print("Bin Width: " + str(bin_range))
# Printing the values
except:
	print("You have not set the min, max, or bins values yet.")