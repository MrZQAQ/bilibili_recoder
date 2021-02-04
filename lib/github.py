# -*- encoding:utf-8 -*-

import requests
import json
import time

imp_class = 'github'

class Remoteinfo():

    def __init__(self,api_url=None):
        self._api_url = api_url
        self._data = None
    
    def decode_api(self,api_url):
        try:
            self._data = requests.get(api_url).json()
        except IOError:
            return False
        return True

    def get_version(self,program_name):
        for assets in self._data["assets"] :
            if assets["name"] == str(program_name) :
                return self._data["tag_name"]
        return False
    
    def get_download_url(self,program_name):
        for assets in self._data["assets"] :
            if assets["name"] == str(program_name) :
                return assets["browser_download_url"]
        return False