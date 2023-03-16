import json
import requests



class WeatherForecast:
    lst_temp_aver = {}

    def __init__(self, keys, city):
        self._keys = keys
        self._city = city
        self._lst = None
        self.lst_get = None
        self.lst_items = None

    def get_weather_data(self):
        res = requests.get('http://api.openweathermap.org/data/2.5/find', params={'q': self._city, 'type': 'like',
                                                                                  'units': 'metric',
                                                                                  'APPID': self._keys})
        self._lst = res.json()

    def get_temperature(self):

        lst_get = self._lst.get('list')
        for i in lst_get:
            self.lst_items = dict(i.items())
            name_city = self.lst_items['name']
            temp_aver = (self.lst_items['main']['temp_min'] + self.lst_items['main']['temp_max']) / 2
            if temp_aver:
                WeatherForecast.lst_temp_aver[name_city] = round(temp_aver, 2)
            else:
                WeatherForecast.lst_temp_aver[name_city] = None
        return WeatherForecast.lst_temp_aver

    def get_description(self):
        lst_get = self._lst.get('list')
        for i in lst_get:
            self.lst_items = dict(i.items())
            descript = self.lst_items['weather']
            if descript:
                return descript
            else:
                return None



