import codecademylib3_seaborn
import pandas as pd

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/queens.csv")

df = pd.DataFrame(streeteasy)

print(df.head())