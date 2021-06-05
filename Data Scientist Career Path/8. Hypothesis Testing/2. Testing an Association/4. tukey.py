from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

# store the data
veryants = pd.read_csv('veryants.csv')
print(veryants)
# run tukey's test
tukey_results = pairwise_tukeyhsd(veryants.Sale, veryants.Store, 0.05)
print(tukey_results)

# determine significance
a_b_significant = True
a_c_significant = False
b_c_significant = False