import  requests



def test_douban():
    new_header = {}
    new_header['Origin'] = 'https://passport.weibo.cn'
    new_header['User-Agent'] =  'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
    new_header['Referer'] = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
    result = requests.get(url="https://www.douban.com", headers=new_header)
    print(result.text)
    print(result.headers)
    print(result.cookies)







if __name__ == '__main__':
    test_douban()

