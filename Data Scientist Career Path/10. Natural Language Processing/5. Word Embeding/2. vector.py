import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

# define score vectors
scores_xavier = np.array([88,92])
scores_niko = np.array([94,87])
scores_alena = np.array([90,48])

# plot vectors
try:
  plt.arrow(0, 0, scores_xavier[0], scores_xavier[1], width=1, color='blue')
except:
  pass
try:
  plt.arrow(0, 0, scores_niko[0], scores_niko[1], width=1, color='orange')
except:
  pass
try:
  plt.arrow(0, 0, scores_alena[0], scores_alena[1], width=1, color='purple')
except:
  pass
plt.axis([0, 100, 0, 100])
plt.show()