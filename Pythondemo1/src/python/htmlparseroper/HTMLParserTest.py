import gzip
from contextlib import closing
from urllib import request
from html.parser import HTMLParser


class EventHTMLParser(HTMLParser):
    content_map = {}

    def __init__(self):
        super().__init__()
        self.tag = ""
        self.name = ""
        self.content = ""
        self.start = False

    def handle_starttag(self, tag, attrs):
        self.tag = tag
        if attrs:
            for attr in attrs:
                if attr[0] == "class":
                    self.name = attr[1]
                    self.start = True

    def handle_data(self, data):
        self.content = data
        if self.name and self.start:
            self.content_map[self.name] = self.content
            self.start = False

def parse_html(url):
    new_req = request.Request(url)
    new_req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    new_req.add_header("Cookie",
                       "_ga=GA1.1.791973393.1725263569; __utmz=32101439.1725263591.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=32101439; __utma=32101439.791973393.1725263569.1732762570.1732775399.3; __utmt=1; __utmb=32101439.3.10.1732775399; _ga_TF35YF9CVH=GS1.1.1732775399.4.1.1732775518.0.0.0")
    with closing(request.urlopen(new_req)) as page:
        page_data = page.read()
        decode_data = gzip.decompress(page_data).decode("utf-8")

    eventHTMLParser = EventHTMLParser()
    eventHTMLParser.feed(decode_data)
    content_map = eventHTMLParser.content_map
    print("会议时间:%s %s" % (content_map.get("date-start"),content_map.get("date-end")))
    print("会议名称:%s" % content_map.get("single-event-title"))
    print("会议地点:%s" % content_map.get("single-event-location"))



if __name__ == "__main__":
    url = "https://www.python.org/events/python-events/1848/"
    parse_html(url)
