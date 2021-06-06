import numpy as np

a = 'spam'
b = 'enhancement'

p_spam = 0.2
p_enhancement_given_spam = 0.05
p_enhancement = 0.05 * 0.2 + 0.001 * (1 - 0.2)
p_spam_enhancement = p_enhancement_given_spam * p_spam / p_enhancement

print(p_spam_enhancement)