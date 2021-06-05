import pandas as pd
import codecademylib3

npi = pd.read_csv("npi_sample.csv")

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print(special_authority_freq)