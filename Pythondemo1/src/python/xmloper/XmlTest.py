from xml.parsers.expat import ParserCreate
from urllib import request


class XmlParser(object):

    content_map = {}

    def __init__(self):
        self.tag = ""
        self.content = ""

    def endElementHandler(self,name):
        self.tag = name
        self.content_map[self.tag] = self.content

    def charsHandler(self,data):
        self.content = data

def parseXml(xml_str):
    parser = ParserCreate()
    xml_parser = XmlParser()
    parser.EndElementHandler = xml_parser.endElementHandler
    parser.CharacterDataHandler = xml_parser.charsHandler
    parser.Parse(xml_str)
    content_map = xml_parser.content_map
    return {
        'city': content_map.get("name"),
        'weather': {
            'condition': 'Sunny',
            'temperature': 37.2,
            'wind': 9.7
        }
    }


# 测试:
URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
