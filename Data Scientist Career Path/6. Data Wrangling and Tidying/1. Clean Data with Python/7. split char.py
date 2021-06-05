import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

name_split = students.full_name.str.split(" ")

students['first_name'] = name_split.str.get(0)

students['last_name'] = name_split.str.get(1)

print(students.head())