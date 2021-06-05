import codecademylib
import pandas as pd

df = pd.read_csv('employees.csv')

total_earned = lambda row: row['hours_worked'] *  row['hourly_wage'] if row['hours_worked'] <= 40 else (40 * row['hourly_wage']) + (row['hours_worked'] - 40) * (row['hourly_wage'] * 1.50)

df['total_earned'] = df.apply(total_earned, axis=1)