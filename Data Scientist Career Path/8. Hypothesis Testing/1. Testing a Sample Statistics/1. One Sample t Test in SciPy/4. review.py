from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

# day 1:
tstat, pval = ttest_1samp(daily_prices[0], 1000)
print("day 1 p-value:")
print(pval)

# 10 days:
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 1000)
  print("day",i+1, "p-value:")
  print(pval)

# 10 days with a different null hypothesis
print("day 1-10 with a different alternative hypothesis:")
for i in range(10):
  tstat, pval = ttest_1samp(daily_prices[i], 950)
  print("day",i+1, "p-value:")
  print(pval)

