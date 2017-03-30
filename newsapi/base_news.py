import requests

from attrdict import AttrDict

class BaseNews(object):
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.payload = {"apiKey": self.API_KEY}
        self.AttrDict = AttrDict
        self.requests = requests
