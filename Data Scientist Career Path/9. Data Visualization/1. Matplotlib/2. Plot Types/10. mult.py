import codecademylib
from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, normed=True)
#plot your other histogram here
plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)

plt.show()