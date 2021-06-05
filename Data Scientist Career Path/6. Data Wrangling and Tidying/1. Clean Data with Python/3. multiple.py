import codecademylib3_seaborn
import pandas as pd
import glob

student_files = glob.glob("exams*.csv")

df_list = []

for files in student_files:
  data = pd.read_csv(files)
  df_list.append(data)

students = pd.concat(df_list)
 
print(students)
print(len(students))