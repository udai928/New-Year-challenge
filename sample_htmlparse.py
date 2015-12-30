# -*-cofing:utf-8-*-
# get target from url by htmlparser

from bs4 import BeautifulSoup
import urllib.request

 
url = 'https://www.microad.co.jp'

req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

links = soup.find_all("a")

for link in links:
    if "http" in link.get("href"):
        print(link.get("href"))
    else:
        print(url + link.get("href"))
