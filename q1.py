'''
What is the most common origin for accidents and how many accidents have
originated there? (2 points) (Note: the origin names on Wikipedia are messy so
a naive count will not be accurate. However, you need not clean them up to
receive full credit for this problem.)
'''
import pandas as pd

data = pd.read_csv('accidents.csv')

#1
data['Flight origin'].value_counts()
print('The the most common origin for accidents is London Heathrow')
