"""
 -*- coding: utf-8 -*-

# Created on Fri Mar  6 17:44:45 2020

# @author: Yap Hui Hsing, WQD180073 (17039525/2)
#          Har Wai San, WQD180025 (17051470/1)
# WQD7005 Data Mining (2019/2020 Semester 2)
# Milestone 1 :  Webcrawling for Stock Data

"""

from bs4 import BeautifulSoup
import requests
import urllib
from datetime import date
import os
import re # regular expression 

# Sector 1 to 20
myurl = 'https://www.malaysiastock.biz/Market-Watch.aspx?type=S&s1={}' 
today = date.today()
print(today)
for sectornum in range(1, 21, 1):
    print(myurl)
    url = myurl.format(sectornum)
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X '
           '10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/72.0.3626.109 Safari/537.36'}
    page_doc = requests.get(url, headers=headers).text    
    soup = BeautifulSoup(page_doc, 'html.parser')
    #soup = BeautifulSoup(page_doc, 'lxml')
    print(soup.prettify())
    sectorname = str(soup.title.string)
    sectorname = sectorname.strip()
    #sector = soup.find_all('label', {"id":"MainContent_lbMarketDesc"})
    print(sectorname)

    table = soup.find_all('table', {"id":"MainContent_tbStockWithAlphabet"})
#    print(table)
         
    test_string = '>(.+?)</td'
    
    try:
        result = re.findall(test_string, str(table[0]))
        print('***RESULT***',len(result))
        #extract tables
        try:
            for i in range(0,len(result),8):
                print(sectornum)
                print(sectorname)
                print(today)
#                print(i,":", result[i])
#                print(i+1,":", result[i+1])
#                print(i+2,":", result[i+2])
#                print(i+3,":", result[i+3])
#                print(i+4,":", result[i+4])
#                print(i+5,":", result[i+5])
#                print(i+6,":", result[i+6])
#                print(i+7,":", result[i+7]) 
        # Stock Code 5281   <a href="Corporate-Infomation.aspx?securityCode=5281">5281</a>
                co_code1 = result[i].split("\">")[1]
                co_code = co_code1.split("<")[0]
                print('COCODE',co_code)
        # <img alt="KLSE MARKET WATCH" src="App_Themes/images/Trend1.ico"/><span><a href="Corporate-Infomation.aspx?securityCode=5281">ADVCON</a></span>
                co_name1 = result[i+1].split("\">")[1]
                co_name = co_name1.split("<")[0]
                print('CONAME',co_name)
                ref = result[i+2]
                open_p = result[i+3]
                last_p = result[i+4]
                change_p = result[i+5]
                change_pc = result[i+6]
                volume = result[i+7]
                row = str(today) + ',' + str(sectornum) + ',' + sectorname +',' + co_code + ',' + co_name + ',' + str(ref) + ',' + str(open_p) + ',' + str(last_p) + ',' + str(change_p) + ',' + str(change_pc) + ',' + str(volume)               
                print('data:',row)
                file = open("output.yhh.csv","a+")
                file.write(row+'\n')
                file.close()
        except:
            print('End of table reached!')
    except:
        print('Financial report not available for this company!')


        
