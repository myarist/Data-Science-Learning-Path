from song_data import songs
import numpy as np

# Define percentile and answer here:
percentile = np.quantile(songs, 0.32)
answer = "below"

#Ignore the code below here:
try:
  print("Your percentile is " + str(percentile) + "\n")
except NameError:
  print("You haven't defined percentile")
