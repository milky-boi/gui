# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:48:55 2019

@author: mile
"""

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
 
 
def Main():
    link = 'https://www.njuskalo.hr/iznajmljivanje-stanova?locationIds=1263%2C1261%2C1262&price%5Bmax%5D=350&livingArea%5Bmin%5D=30'
    Scrape(link)
 
def Scrape(link):
    ua = UserAgent()
    print(ua.random)
    response = requests.get(link, headers = {'User-Agent' : ua.random})
    content = BeautifulSoup(response.content, 'html.parser')
    
    #soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = content.find('article', attrs={'class':'entity-body'})
    
    name = name_box.text.strip() # strip() is used to remove starting and trailing
    print (name)
    
    # get the index price
    price_box = content.find('class', attrs={'class':'entity-description-main'})
    price = price_box.text
    print (price)
    
    with open('output.html', "w", encoding="utf-8") as f:
        f.write(response.text)
 
if __name__ == '__main__':
    Main()