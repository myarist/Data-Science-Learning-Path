import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print(visits)
print(checkouts)

v_to_c = visits.merge(checkouts)

v_to_c['time'] = v_to_c.checkout_time - \
                 v_to_c.visit_time
 
print(v_to_c)

print(v_to_c.time.mean())