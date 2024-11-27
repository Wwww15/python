from contextlib import closing
from urllib.request import urlopen


def fetch_url():
    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)


def fetch_url_two():
    with closing(urlopen('https://www.taobao.com')) as page:
        htmls = page.read()
        htmls = htmls.decode('utf-8')
        print(htmls)


if __name__ == '__main__':
    fetch_url_two()

