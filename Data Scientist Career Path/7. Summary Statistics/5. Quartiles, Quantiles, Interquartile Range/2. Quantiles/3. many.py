from song_data import songs
import numpy as np

# Define quartiles, deciles, and tenth here:
quartiles = np.quantile(songs, [0.25, 0.5, 0.75])
deciles = np.quantile(songs, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

tenth = 3

#Ignore the code below here:
try:
  print("The quariles are " + str(quartiles) + "\n")
except NameError:
  print("You haven't defined quartiles.\n")
try:
  print("The deciles are " + str(deciles) + "\n")
except NameError:
  print("You haven't defined deciles.\n")
