import numpy as np

p_positive_given_disease = (0.99 * (.00001))/ (1./100000.)
print(p_positive_given_disease)

p_disease = 1./100000.
print(p_disease)

p_positive = (0.00001) + (0.01) 
print(p_positive)

p_disease_given_positive = (p_positive_given_disease) * (p_disease) / (p_positive)

print(p_disease_given_positive)