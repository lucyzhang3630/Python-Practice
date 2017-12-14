 # --coding:utf-8 --

from urllib import request, parse

def fetch_xml(url):
    f = request.urlopen(url)
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))


# test
print(fetch_xml('https://www.python.org/events/python-events/'))


# a better solution
#!/usr/bin/env python3
#! _*_ coding:utf-8 _*_
import re
from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    def __init__(self):
        self.today = 0
        self.__data = {}

    @property
    def get_data(self):
        return self.__data

    def satrt_element(self,name,attrs):
        if name == "yweather:location":
            self.__data['city'] = attrs['city']
            self.__data['country'] = attrs['country']
        if name == "yweather:condition":
            self.today = re.split(r'\s?', attrs['date'])[1]
        if name == "yweather:forecast":
            if re.split(r'\s?', attrs['date'])[0] == self.today:
                self.__data['today'] = {}
                self.__data['today']['text'] = attrs['text']
                self.__data['today']['low'] = int(attrs['low'])
                self.__data['today']['high'] = int(attrs['high'])
            if int(re.split(r'\s?', attrs['date'])[0]) == int(self.today) + 1:
                self.__data['tomorrow'] = {}
                self.__data['tomorrow']['text'] = attrs['text']
                self.__data['tomorrow']['low'] = int(attrs['low'])
                self.__data['tomorrow']['high'] = int(attrs['high'])

    def end_element(self,name):
        pass

    def char_data(self,text):
        pass


class get_weather(object):
    def __init__(self,city):
        self._city = city

    @staticmethod
    def get_yahoo(city):
        url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + city +"%22)&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        with request.urlopen(url) as f:
            data = f.read()
        return data

    def parse_weather(self):
        handler = DefaultSaxHandler()
        parser = ParserCreate()
        parser.StartElementHandler = handler.satrt_element
        parser.EndElementHandler = handler.end_element
        parser.CharacterDataHandler = handler.char_data
        parser.Parse(self.get_yahoo(self._city))
        return str(handler.get_data)


weather = get_weather("shanghai").parse_weather()
print(weather)
