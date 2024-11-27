from xml.parsers.expat import ParserCreate
from urllib import request

def parseXml(xml_str):
    parser = ParserCreate()

    return {
        'city': '?',
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