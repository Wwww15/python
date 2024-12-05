import socket
import threading
import time


def socket_server(addr, port):
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.bind((addr, port))
    s_server.listen(10)
    while True:
        sock, arr = s_server.accept()
        threading.Thread(target=socket_process, args=(sock, arr)).start()


def socket_process(sock: socket.socket, addr):
    print("位于 %s 的客户端已经连接上" % addr[0])
    while True:
        re_data = sock.recv(1024)
        if re_data:
            print("热烈欢迎 %s" % re_data.decode("utf-8"))
            time.sleep(2)
            sock.send("再来玩啊!".encode("utf-8"))
        else:
            break
    sock.close()


if __name__ == "__main__":
    addr = "127.0.0.1"
    port = 9999
    socket_server(addr, port)
