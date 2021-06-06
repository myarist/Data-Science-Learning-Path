import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

# Create your log_odds() function here
def log_odds(features,coefficients,intercept):
  return np.dot(features,coefficients) + intercept

# Calculate the log-odds for the Codecademy University data here
calculated_log_odds = log_odds(hours_studied,calculated_coefficients,intercept)

print(calculated_log_odds)
print(hours_studied)