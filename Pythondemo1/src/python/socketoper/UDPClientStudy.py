import socket


def socket_client(addr, port):
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s = "张三".encode("utf-8")
    print(" %s 来啦" % "张三")
    c_socket.sendto(s, (addr, port))
    r_data = c_socket.recv(1024)
    print(r_data.decode("utf-8"))
    c_socket.close()


if __name__ == "__main__":
    socket_client("localhost",9999)
