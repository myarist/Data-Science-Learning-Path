import codecademylib3

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Set a correct value for num_tests_50percent
num_tests_50percent = 15


# Create the plot
sig_threshold = 0.10
num_tests = np.array(range(50))
probabilities = 1-((1-sig_threshold)**num_tests)
plt.plot(num_tests, probabilities)

# Edit title and axis labels
plt.title('Type I Error Rate for Multiple Tests', fontsize=15)
# Label the y-axis
plt.ylabel('Probability of at Least One Type I Error', fontsize=12)
# Label the x-axis
plt.xlabel('Number of Tests', fontsize=12)

# Show the plot                
plt.show()