"""
Module for koinex upstream
"""
import requests
from django.utils import timezone as dj_timezone


class KoinexDriver:
    """Driver class for koinex upstream"""

    def __init__(self):
        self.__latest = {}
        self.__url = 'https://koinex.in/api/ticker'
        self.__time_of_update = None

    def get_data(self):
        """Returns latest data"""
        return self.__latest

    def get_time_of_update(self):
        """Provides last updated data"""
        return self.__time_of_update

    def get_latest_updates(self):
        """Refreshes the data from upstream and updates last updated time"""
        try:
            response = requests.get(self.__url)
            if response.ok:
                self.__latest = response.json()
                self.__time_of_update = dj_timezone.now()
        except:
            pass
        return self.get_data(), self.get_time_of_update()

    def get_coin_details(self, coin):
        """Provides value and stats for a particular coin"""
        try:
            return dict(
                value=self.__latest['prices']['inr'][coin],
                stats=self.__latest['stats']['inr'][coin]
            )
        except KeyError:
            raise Exception("No Data Found")


koinex = KoinexDriver()
