# -*- coding: utf-8 -*-
#Note 1: be careful with array indexing
#Note 2:children need to call the constructor function of their parent
#Note 3: the attrs of HTMLParser is a list with element as tuple
#Note 4：when calling the class attribute, need to use 'self', or it equals declaring a new variable

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self._event_title = []
        self._event_location = []
        self._ecent_time = []
        self._reading_title = False
        self._reading_time = False
        self._reading_location = False

    #analyze the header
    def handle_starttag(self, tag, attrs):
        if tag == 'time':
            self._reading_time = True
        if len(attrs) >= 1:
            if tag == 'h3' and attrs[0][1] == 'event-title':
                self._reading_title = True
            if tag == 'span' and attrs[0][1] == 'event-location':
                self._reading_location = True

    #analyze the content
    def handle_data(self, data):
        if self._reading_title:
            self._event_title.append(data)
            self._reading_title = False
        if self._reading_time:
            self._ecent_time.append(data)
            self._reading_time = False
        if self._reading_location:
            self._event_location.append(data)
            self._reading_location = False

    @property
    def data(self):
        self._data = []
        for i in range(len(self._event_title)):
            dic = {}
            dic["title"] = self._event_title[i]
            dic["time"] = self._ecent_time[i]
            dic["location"] = self._event_location[i]
            self._data.append(dic)
        return self._data

def getHtml():
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        data = f.read().decode('utf-8')
    return data

parser = MyHTMLParser()
parser.feed(getHtml())
for item in parser.data:
    print(str(item))
