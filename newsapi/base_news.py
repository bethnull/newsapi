import requests
from abc import ABCMeta, abstractproperty
from attrdict import AttrDict

class BaseNews(object):
    __metaclass__ = ABCMeta

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.payload = {"apiKey": self.API_KEY}

    @abstractproperty
    def endpoint(self):
        raise NotImplemented

    def get(self, attributes_format=True):
        r = requests.get(self.endpoint, params=self.payload)
        if r.status_code != 200:
            raise BaseException("Either server didn't respond or has resulted in zero results.")
        try:
            content = r.json()
        except ValueError:
            raise ValueError("No json data could be retrieved.")
        if attributes_format:
            return AttrDict(content)
        return content
