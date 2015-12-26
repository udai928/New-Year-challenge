# -*-cofing:utf-8-*-
# get target from url by htmlparser

from bs4 import BeautifulSoup
import urllib.request

# 
url = 'http://www.amazon.co.jp/gp/registry/wishlist/BCSQ72LZSFIU/ref=topnav_lists_1'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")
# you must add '_' after 'class'
#favorite_elements = soup.find_all('h5')

favorite_elements = soup.find_all("div",class_="a-text-left a-fixed-left-grid-col a-col-right")

for favorite_element in favorite_elements:
    print(favorite_element.a.string)
    favorite_price_elements = favorite_element.find_all("div",class_="a-section price-section")
    for favorite_price_element in favorite_price_elements:
        favorite_price_span = favorite_price_element.find('span')
        print(favorite_price_span.text)

    print("#######################################")
