'''
Which air operator has had the most fatalities and how many?
Hint: Use `groupby`. (4 points)
'''

import pandas as pd

flights = pd.read_csv('accidents2.csv')

values = flights.sort_values('Fatalities count', ascending=False).head(1)
print('The Flight With the Most Fatalities is:', flights)
