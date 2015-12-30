# -*-coding:utf-8-*-
import config

class Conf:
    def __init__(self, confKEY):
        self.TARGETURL = config.SETTINGS.get(confKEY).get('TARGETURL')

    def setTARGETURL(self,TARGETURL):
        self.TARGETURL = TARGETURL

    def getTARGETURL(self):
        return self.TARGETURL
