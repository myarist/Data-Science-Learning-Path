import codecademylib3_seaborn
import pandas as pd
from students import students

students.score = students['score'].replace('%', '', regex=True)

students.score = pd.to_numeric(students.score)