from riotwatcher import LolWatcher, ApiError
import pandas as pd

class Connect:
    def __init__(self, api_key, region):
        self.__api_key = api_key
        self.__region = region
        self.__watcher = LolWatcher(api_key)

    @property
    def region(self):
        return self.__region
