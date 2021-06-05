import codecademylib3
import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv")
dist_2 = np.genfromtxt("2.csv")

#calculate ratio of standard deviations:
ratio = np.std(dist_1) / np.std(dist_2)
print(ratio)

#check normality assumption
normal_assumption = True

#plot histograms of each distribution
plt.hist(dist_1, alpha = .8, normed = True, label = 'dist 1')
plt.hist(dist_2, alpha = .8, normed = True, label = 'dist 2')
plt.legend()
plt.show()