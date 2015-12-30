#-*-coding:utf-8-*-

import omusubiModel
import omusubiUtil
from datetime import datetime


def main():
    print ("START omusubi." + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    amazonHtmlParser()
    print ("END omusubi." + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))


def amazonHtmlParser():

    htmlObjs = omusubiUtil.getHtmlObjsFromConf('amazon')

    for htmlObj in htmlOjbs:
        favorite_elements = htmlObj.find_all("div",class_="a-text-left a-fixed-left-grid-col a-col-right")

        for favorite_element in favorite_elements:
            print(favorite_element.a.string)
            favorite_price_elements = favorite_element.find_all("div",class_="a-section price-section")
            for favorite_price_element in favorite_price_elements:
                favorite_price_span = favorite_price_element.find('span')
                print(favorite_price_span.text)


if __name__ == '__main__' :
    main()
