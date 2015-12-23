# -*-cofing:utf-8-*-
# get target from url by htmlparser

from bs4 import BeautifulSoup
import urllib.request

# 
url = 'http://finance.yahoo.co.jp/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")
# you must add '_' after 'class'
nikkei_url = soup.find('dt',class_="title floatL")

print(nikkei_url)
