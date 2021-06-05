from song_data import songs
import numpy as np

#Create the variables songs_q1, songs_q2, and songs_q3 here:
songs_q1 = np.quantile(songs, 0.25)
songs_q2 = np.quantile(songs, 0.5)
songs_q3 = np.quantile(songs, 0.75)

favorite_song = 100
quarter = 1

#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(songs_q1) + " seconds")
except NameError:
  print("You haven't defined songs_q1")
try:
  print("The second quartile of dataset one is " + str(songs_q2)+ " seconds")
except NameError:
  print("You haven't defined songs_q2")
try:
  print("The third quartile of dataset one is " + str(songs_q3)+ " seconds")
except NameError:
  print("You haven't defined songs_q3\n")