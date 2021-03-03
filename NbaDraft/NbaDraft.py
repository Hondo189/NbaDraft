import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# pulling in html from the website below  which contains the "best available" draft board. 
r= requests.get('https://www.espn.com/nba/draft/bestavailable')

#convert request to BeautfiflSoup object for extracting relevant data
soup = bs(r.content,features="lxml")
#print(type(soup))

# List to be used for API calls
datalist = 	['draftTable__headline draftTable__headline--pick',
	'draftTable__headline draftTable__headline--team',
	'draftTable__headline draftTable__headline--player',
	'draftTable__headline draftTable__headline--school']

# empty objects, will be asigned BeautifulSoup results objects
pick = ''
team = ''
player = ''
school = ''


# empty lists to be looped through and populated with draft data
pickList = []
teamList = []
playerList = []
schoolList = []

#List of variables to loop through to call 
colList = [pick,
           team,
           player,
           school]

# These will become the lists with the extracted data
lists = [pickList,
          teamList,
          playerList,
          schoolList]

#Create DraftBoard DataFrame
df2 = pd.DataFrame()

#Looping to create functions to call for draftboard info
for n, row in enumerate(datalist):
    colList[n] = soup.find_all("span", attrs={"class": row})
    for elem in colList[n]:
        lists[n].extend(elem)
        #print(m)
#print(lists)
#print(type(colList[0]))

#for n, row in enumerate(lists):
    #if n != 1:
        #print(var)
        #for m, elem in enumerate(row):
            #print(elem)

for column in zip(*lists):
    for n, elem in enumerate(column):
        if n != 1:
            print(elem,end=' ')
    print()