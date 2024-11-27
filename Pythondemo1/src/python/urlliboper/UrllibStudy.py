from urllib import request


def request_douban():
    with request.urlopen('https://www.baidu.com/') as f:
        data = f.read();
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        decode = data.decode("utf-8")
        print("Data:", decode)


def request_iphone():
    request_data = request.Request('https://www.baidu.com/')
    request_data.add_header("User-Agent",
                            "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, "
                            "like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
    with request.urlopen(request_data) as r:
        data = r.read()
        for k, v in r.getheaders():
            print('%s: %s' % (k, v))
        decode_data = data.decode("utf-8")
        print("Data:", decode_data)


if __name__ == '__main__':
    # request_douban()
    request_iphone()
