import codecademylib3_seaborn
from song_data import songs
import matplotlib.pyplot as plt

plt.hist(songs, bins = 200)
plt.axvline(x=364, label="Chicago", c = 'r')
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.legend()
plt.show()