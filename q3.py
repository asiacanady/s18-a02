import pandas as pd
import re
data = pd.read_csv('accidents.csv')


def get_first_number(text):
    if text != None:
        fatalities_list = []
        pattern = re.compile('\d+')
        deaths = pattern.findall(text)
        if deaths == []:
            deaths = None
        else:
            deaths = float(deaths[0])
    else:
        deaths = None
    return deaths

data['Fatalities count'] = data[data['Fatalities'].isnull()==False]['Fatalities'].apply(fatalscount)
print(data['Fatalities count'])
data.to_csv('accidents2.csv')
