#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 9 - Apple Stock"""

from bs4 import BeautifulSoup
import urllib2, csv

def webpage(web_link):
    read_webpagedata = urllib2.urlopen(web_link)
    webpage = BeautifulSoup(read_webpagedata, "html.parser")
    return webpage

url = webpage("https://www.nasdaq.com/symbol/aapl/historical")

i = 1
find_tr = url.findAll('tr')
for find_td in find_tr:

    try:

        table_data = find_td.findAll('td')
        stock_date = str(table_data[0].get_text())
        stock_close_price = str(table_data[4].get_text())
        print(i, "Date: " + stock_date, "Close Price: " + stock_close_price)
        i = i + 1
    except:
        continue
