import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

score_mean = students.score.mean()

students['score'] = students['score'].fillna(0)

score_mean_2 = students.score.mean()