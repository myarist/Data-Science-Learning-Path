import numpy as np
import pandas as pd
from scipy.stats import binom_test

# calculate p_value_2sided here:
p_value_2sided = binom_test(41, n=500, p=0.1)
print(p_value_2sided)

# calculate p_value_1sided here:
p_value_1sided = binom_test(41, n=500, p=0.1, alternative = 'less')
print(p_value_1sided)