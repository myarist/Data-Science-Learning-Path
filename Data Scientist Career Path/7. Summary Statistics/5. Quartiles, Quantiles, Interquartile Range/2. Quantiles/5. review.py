import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from data import school_one, school_two, school_three

deciles_one = np.quantile(school_one, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
deciles_two = np.quantile(school_two, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
deciles_three = np.quantile(school_three, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

plt.subplot(311)
plt.hist(school_one)
for decile in deciles_one:
  plt.axvline(x=decile, c = 'r')
plt.title("School One")
plt.xlabel("SAT Score")
  
plt.subplot(312)
plt.hist(school_two)
for decile in deciles_two:
  plt.axvline(x=decile, c = 'r')
plt.title("School Two")
plt.xlabel("SAT Score")
  
plt.subplot(313)
plt.hist(school_three)
for decile in deciles_three:
  plt.axvline(x=decile, c = 'r')
plt.title("School Three")
plt.xlabel("SAT Score")
plt.tight_layout()
plt.show()