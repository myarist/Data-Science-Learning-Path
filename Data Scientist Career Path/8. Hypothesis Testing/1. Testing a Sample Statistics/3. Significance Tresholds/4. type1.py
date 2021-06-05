import codecademylib3

# Import libraries
import numpy as np
from scipy.stats import binom_test

# Initialize num_errors
false_positives = 0
# Set significance threshold value
sig_threshold = 0.05

# Run binomial tests & record errors
for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.8, 0.2])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, .8)
    if p_val < sig_threshold:
        false_positives += 1

# Print proportion of type I errors 
print(false_positives/1000)