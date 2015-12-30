#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib.request
import sys
import omusubiModel

def getHtmlObj(TARGETURL):
    TARGETURLs = omusubiModel.getTARGETURL()
    try:
        request = urllib.request.Request(TARGETURL)
        response = urllib.request.urlopen(request)
        html = response .read()
        htmlObj = BeautifulSoup(html,"lxml")
    except:
        print("failed. get html..")
        sys.exit(1)
    return htmlObj


def getHtmlObjsFromConf(confKey):
    confObj = omusubiModel.Conf(confKey)
    TARGETURLs = confObj.getTARGETURL()
    htmlObjs = [] 
    for TARGETURL in TARGETURLs:
        htmlObjs.append(getHtmlObj(TARGETURL))
    return htmlObjs


def getHtmlObjsFromPath(fullPath):
    TARGETURLs = getUrl(fullPath)
    htmlObjs = []
    for TARGETURL in TARGETULRs:
        htmlObjs.append(getHtmlObj(TARGETURL))
    return htmlObjs


def getUrl(fullPath):
    try:
        file = open(fullPath,"r",encoding="UTF-8")
        lines = file.readlines()
    except:
        print("failed. read file..")
        sys.exit(1)
    return lines
