import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

difference_one = grades[0] - mean
difference_two = grades[1] - mean
difference_three = grades[2] - mean
difference_four = grades[3] - mean
difference_five = grades[4] - mean


# IGNORE CODE BELOW HERE
print("The mean of the data set is " + str(mean) + "\n")
print("The first student is " +str(round(difference_one, 2)) + " percentage points away from the mean.")
print("The second student is " +str(round(difference_two, 2)) + " percentage points away from the mean.")
print("The third student is " +str(round(difference_three, 2)) + " percentage points away from the mean.")
print("The fourth student is " +str(round(difference_four, 2)) + " percentage points away from the mean.")
print("The fifth student is " +str(round(difference_five, 2)) + " percentage points away from the mean.")