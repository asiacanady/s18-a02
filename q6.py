'''
Make a line plot where the x axis the year and the y axis is the number of
accidents in that year. Save it as `years.png`. (4 points)

Hint: Some of the dates are missing or formatted poorly so you can pass the
argument `errors='coerce'` to [`pd.to_datetime()`]
(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html)
to simply convert them to `NaT`
("Not a Time",  the equivalent for times of `NaN` for numbers).
'''

import pandas as pd
import matplotlib.pyplot as plt

import datetime

accidents = pd.read_csv('accidents.csv')

accidents['year'] = pd.to_datetime(accidents['Date'], errors='coerce').dt.year

print(accidents['year'])

a = accidents['year'].value_counts().reset_index()
a.columns = ['Year', 'Accidents']
b = a.sort_values('Year', ascending= False)
plt.plot(b['Year'], b['Accidents'])
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.show()
plt.savefig('years.png')
