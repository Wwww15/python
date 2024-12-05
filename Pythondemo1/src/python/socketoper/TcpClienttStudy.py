import socket


def socket_client(addr, port):
    s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_client.connect((addr, port))
    s_client.send("小李".encode("utf-8"))
    buff_size = 1024
    result_msg = s_client.recv(buff_size)
    print(result_msg.decode("utf-8"))


if __name__ == "__main__":
    addr = "127.0.0.1"
    port = 9999
    socket_client(addr, port)
