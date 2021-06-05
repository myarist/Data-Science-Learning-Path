import numpy as np
import pandas as pd
from scipy.stats import binom_test

def simulation_binomial_test(observed_successes, n, p, alternative_hypothesis):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  null_outcomes = np.array(null_outcomes)

  if alternative_hypothesis == 'less':
    p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  elif alternative_hypothesis == 'greater':
    p_value = np.sum(null_outcomes >= observed_successes)/len(null_outcomes)
  else:
    difference = np.abs(p*n - observed_successes)
    upper = p*n + difference
    lower = p*n - difference
    p_value = np.sum((null_outcomes >= upper) | (null_outcomes <= lower))/len(null_outcomes)
  
  #return the p-value
  return p_value

#Test your function:
print('lower tail one-sided test:')
p_value1 = simulation_binomial_test(45, 500, .1, alternative_hypothesis = 'less')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)

print('upper tail one-sided test:')
p_value1 = simulation_binomial_test(53, 500, .1, alternative_hypothesis = 'greater')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(53, 500, .1, alternative = 'greater')
print("binom_test p-value: ", p_value2)

print('two-sided test:')
p_value1 = simulation_binomial_test(42, 500, .1, alternative_hypothesis = 'not_equal')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(42, 500, .1)
print("binom_test p-value: ", p_value2)