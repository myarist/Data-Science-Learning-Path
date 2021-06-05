import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)

# calculate the chi squared statistic and save it as chi2, then print it:
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)
print(chi2)