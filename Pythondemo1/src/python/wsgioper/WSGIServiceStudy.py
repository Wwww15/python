from wsgiref.simple_server import make_server
from WSGIClientStudy import hello


def server():
    web_server = make_server('', 8080, hello)
    web_server.serve_forever()




if __name__ == "__main__":
    server()
