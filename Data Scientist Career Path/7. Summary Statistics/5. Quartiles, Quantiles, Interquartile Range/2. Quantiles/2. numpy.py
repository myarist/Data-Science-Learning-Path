from song_data import songs
import numpy as np

# Define twenty_third_percentile here:
twenty_third_percentile = np.quantile(songs, 0.23)

#Ignore the code below here:
try:
  print("The value that splits 23% of the data is " + str(twenty_third_percentile) + "\n")
except NameError:
  print("You haven't defined twenty_third_percentile.")
