import codecademylib3_seaborn
from song_data import songs
import matplotlib.pyplot as plt
import numpy as np

q1 = np.quantile(songs, 0.25)
q2 = np.quantile(songs, 0.5)
q3 = np.quantile(songs, 0.75)

plt.hist(songs, bins = 200)
plt.axvline(x=q1, label="Q1", c = '#6400e4')
plt.axvline(x=q2, label="Q2", c = '#fd4d3f')
plt.axvline(x=q3, label="Q3", c = '#4fe0b0')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.legend()
plt.show()