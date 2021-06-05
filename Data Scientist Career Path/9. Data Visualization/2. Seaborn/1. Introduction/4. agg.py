import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

gradebook = pd.read_csv('gradebook.csv')
print(gradebook)

assignment1 = gradebook[gradebook.assignment_name == 'Assignment 1']
print(assignment1)

asn1_median = np.median(assignment1.grade)
print(asn1_median)