#!user/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 9 - Fotball Stats"""


from bs4 import BeautifulSoup
import urllib2, csv

def webpage(web_link):
    read_webpagedata = urllib2.urlopen(web_link)
    webpage = BeautifulSoup(read_webpagedata, "html.parser")
    return webpage


url = webpage("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns")

i = 1
find_tr = url.findAll('tr')
for find_td in find_tr:
    try:
        if i <= 20:
            table_data = find_td.findAll('td')
            player = table_data[0].get_text()
            position = table_data[1].get_text()
            team = table_data[2].get_text()
            touchdown = table_data[6].get_text() 

            print(i,  "Player: " + str(player) +  ", Position: " +  str(position) +  ", Team: " +  str(team) +  ", TouchDown: " +  str(touchdown))
            i = i + 1
        else:
            break
        
    except:
        continue
