import codecademylib3_seaborn
from song_data import songs
import matplotlib.pyplot as plt
import numpy as np

q1 = np.quantile(songs, 0.25)
q2 = np.quantile(songs, 0.5)
q3 = np.quantile(songs, 0.75)

plt.subplot(3,1,1)
plt.hist(songs, bins = 200)
plt.axvline(x=q1, c = 'r')
plt.axvline(x=q2, c = 'r')
plt.axvline(x=q3, c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.title("4-Quantiles")

plt.subplot(3,1,2)
plt.hist(songs, bins = 200)
plt.axvline(x=np.quantile(songs, 0.2), c = 'r')
plt.axvline(x=np.quantile(songs, 0.4), c = 'r')
plt.axvline(x=np.quantile(songs, 0.6), c = 'r')
plt.axvline(x=np.quantile(songs, 0.8), c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.title("5-Quantiles")

plt.subplot(3,1,3)
plt.hist(songs, bins = 200)
for i in range(1, 10):
  plt.axvline(x=np.quantile(songs, i/10), c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.title("10-Quantiles")

plt.tight_layout()
plt.show()