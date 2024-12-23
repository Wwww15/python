import socket


def socket_server(addr, port):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s_socket.bind((addr, port))
    while True:
        data, addr = s_socket.recvfrom(1024)
        s = "Hello %s, welcome to this city" % data.decode("utf-8")
        print(s)
        s_socket.sendto(s.encode("utf-8"), addr)


if __name__ == "__main__":
    socket_server("localhost", 9999)
