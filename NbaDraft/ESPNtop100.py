import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def scrapeESPN(url, lists):
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
    #List of variables to loop through to call 
    colList = [pick,
               team,
               player,
               school]
    
    r = requests.get(url)
    soup = bs(r.content,features="lxml")

    for n, row in enumerate(datalist):
        colList[n] = soup.find_all("span", attrs={"class": row})
        for elem in colList[n]:
            lists[n].extend(elem)
    return lists
