import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

#When calculating these variables, square the difference.
difference_one = (88 - mean) ** 2
difference_two = (82 - mean) ** 2
difference_three = (85 - mean) ** 2
difference_four = (84 - mean) ** 2
difference_five = (90 - mean) ** 2

difference_sum = difference_one + difference_two + difference_three + difference_four + difference_five

variance = difference_sum / 5

print("The sum of the squared differences is " + str(difference_sum))
print("The variance is " + str(variance))