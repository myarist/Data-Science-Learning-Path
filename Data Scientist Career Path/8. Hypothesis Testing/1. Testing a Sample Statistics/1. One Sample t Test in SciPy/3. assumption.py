import codecademylib3
import numpy as np
import matplotlib.pyplot as plt

prices = np.genfromtxt("prices.csv")

#plot your histogram here
plt.hist(prices)
plt.show()