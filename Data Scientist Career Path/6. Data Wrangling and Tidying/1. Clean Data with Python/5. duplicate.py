import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

duplicates = students.duplicated()

print(duplicates.value_counts())

students = students.drop_duplicates()

duplicates = students.duplicated()

print(duplicates.value_counts())