# -*-cofing:utf-8-*-

from bs4 import BeautifulSoup
import urllib.request
import time

def main():
    start_time = time.time()
    print ("START omusubi.  ",time.ctime())
    html_parser_links()
    end_time = time.time()
    print ("END omusubi. ",time.ctime())    
    print ("Processing time is %f" %(end_time - start_time) +"s.")

def html_parser_links():
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

    

if __name__ == '__main__':
    main()
