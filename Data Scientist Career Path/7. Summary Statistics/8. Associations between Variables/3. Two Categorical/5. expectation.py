import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print("observed contingency table:")
print(special_authority_freq)

# calculate the expected contingency table if there's no association and save it as expected
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)


# print out the expected frequency table
print("expected contingency table (no association):")
print(np.round(expected))
