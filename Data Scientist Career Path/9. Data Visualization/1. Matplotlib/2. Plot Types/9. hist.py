import codecademylib
from matplotlib import pyplot as plt
from script import sales_times

#create the histogram here
plt.hist(sales_times, bins=20)
plt.show()