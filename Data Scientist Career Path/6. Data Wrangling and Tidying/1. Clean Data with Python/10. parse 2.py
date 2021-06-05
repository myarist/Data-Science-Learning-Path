import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

print(students.grade)

students.grade = students.grade.replace('\w\w grade', '', regex=True)

print(students.dtypes)

students.grade = pd.to_numeric(students.grade)

avg_grade = students.grade.mean()

print(avg_grade)