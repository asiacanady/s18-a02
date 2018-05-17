#import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#start the soup
base='https://en.wikipedia.org'
path= '/wiki/List_of_accidents_and_incidents_involving_commercial_aircraft'
response=requests.get(base+path)
page = BeautifulSoup(response.text, 'html.parser')

#find all of the bolds
bold= page.find_all('b')
bold_list=bold[:-1]

#iterate dictionary and create empty list
d={}
last_list=[]

#write a function that scrape the list of flights with header information
def getTable(last_list):
    for b in bold_list:
        a = b.find('a')
        if a!=None:
            path =a.attrs['href']
            response =requests.get(base+path)
            lists = BeautifulSoup(response.text, 'html.parser')
            d['Name']=a.attrs['title']
            headers = ['Date', 'Operator', 'Flight origin', 'Destination', 'Fatalities']

            for header in headers:
              data = lists.find('th', text=header)
              if data!=None:
                 data2 = data.find_next('td').text
                 d[header] = data2
            last_list.append(d.copy())

    print(last_list)

#clean the list to remove extraneous information
def getTable(page, header):
    clean = BeautifulSoup(response.get(page), 'html.parser')
    r = clean.find(header)
    r.text

date_string = 'August\xa02,\xa01999(1998-02-98)'
date_string.replace('\xa0', ' ')

#look at the data
last_list

#save the data to a csv file
data_frame =pd.DataFrame(last_list).drop_duplicates()
data_frame.to_csv('accidents.csv', index=False)
