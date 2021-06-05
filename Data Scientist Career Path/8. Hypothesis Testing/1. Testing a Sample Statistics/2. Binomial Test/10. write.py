import numpy as np
import pandas as pd
from scipy.stats import binom_test

def simulation_binomial_test(observed_successes, n, p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(observed_successes):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= 41)/len(null_outcomes) 
  
  #return the p-value
  return p_value

#Test your function below by uncommenting the code below. You should see that your simulation function gives you a very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)
