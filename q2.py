'''
Which operator has had the most accidents and how many? (2 points)
'''

import pandas as pd
data = pd.read_csv('accidents.csv')

data['Operator'].value_counts()
print('The operator with the most accidents is Aeroflot with 31 accidents')
