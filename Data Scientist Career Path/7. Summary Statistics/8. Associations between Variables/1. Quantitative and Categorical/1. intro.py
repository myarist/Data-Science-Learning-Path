import numpy as np
import pandas as pd
import codecademylib3

students = pd.read_csv('students.csv')

#print the first five rows of students:
print(students.head())

#separate out scores for students who live in urban and rural locations:
scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']