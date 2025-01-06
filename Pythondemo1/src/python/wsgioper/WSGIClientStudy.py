

def hello(environ,start_response):
    request_method = environ["REQUEST_METHOD"]
    path_info = environ["PATH_INFO"]
    print("当前请求方式:",request_method)
    print("当前请求地址:",path_info)
    start_response('200 ok', [("Content-Type","text/html")])
    return [b'<h1>Hello,web!</h1>']

