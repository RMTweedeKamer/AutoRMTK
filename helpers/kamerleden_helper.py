import os
import urllib
import json
from functools import lru_cache

class KamerledenHelper(object):
    __result = None

    @staticmethod
    def tweede_kamerleden() -> list:
        return KamerledenHelper.get()['tweedeKamer']

    @staticmethod
    def eerste_kamerleden() -> list:
        return KamerledenHelper.get()['eersteKamer']

    def get():
        url = os.getenv('KAMERLEDEN_URL')
        r = urllib.request.urlopen(url)
        return json.loads(r.read())


