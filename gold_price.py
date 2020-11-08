# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:20:47 2020

@author: winia
"""
import time
import bs4
import requests
from bs4 import BeautifulSoup

def parsePrice():
    r=requests.get('https://www.coininvest.com/pl/wykresy/kurs-zlota/')
    soup=bs4.BeautifulSoup(r.text,'xml')
    price=soup.find('div',{'class':'live_metal_prices_li_in'}).find('span').text
    return price


while True:
    print('Aktualna cena złota za uncje to :  ' + parsePrice())
    time.sleep(5)    

