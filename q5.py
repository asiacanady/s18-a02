'''
Which air operator has had the most fatalities and how many? Hint: Use `groupby`.
'''
import pandas as pd
import re
accidents = pd.read_csv('accidents2.csv')

accidents_grouped = accidents.groupby('Operator')['Fatalities count'].sum().reset_index()
count = accidents_grouped.sort_values('Fatalities count', ascending= False)

print('The operateor with the most fatalities is', count.head(1))
