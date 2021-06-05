from song_data import songs
import numpy as np

q1 = np.quantile(songs, 0.25)
#Create the variables q3 and interquartile_range here:
q3 = np.quantile(songs, 0.75)
interquartile_range = q3 - q1

# Ignore the code below here
try:
  print("The first quartile of the dataset is " + str(q1) + "\n")
except NameError:
  print("You haven't defined q1 yet\n")
  
try:
  print("The third quartile of the dataset is " + str(q3) + "\n")
except NameError:
  print("You haven't defined q3 yet\n")
  
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")