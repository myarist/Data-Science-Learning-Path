import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
from data import dataset_one, dataset_two

plt.hist(dataset_one, alpha =0.75, label = "dataset_one", bins = 80)
plt.hist(dataset_two, alpha = 0.5, label = "dataset_two", bins = 80)
plt.legend()

print("The mean of the first dataset is " + str(np.mean(dataset_one)))
print("The mean of the second dataset is " + str(np.mean(dataset_two)) + "\n")

print("The variance of the first dataset is " + str(np.var(dataset_one)))
print("The variance of the second dataset is " + str(np.var(dataset_two)))

plt.show()
