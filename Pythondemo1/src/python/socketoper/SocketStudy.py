import socket
import threading


def socket_client(addr, port):
    s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_client.connect((addr, port))
    s_client.send("小李".encode("utf-8"))
    buff_size = 1024
    result_msg = s_client.recv(buff_size)
    print(result_msg.decode("utf-8"))



def socket_server(addr, port):
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.bind((addr,port))
    s_server.listen(5)
    while True:
        sock,arr = s_server.accept()
        threading.Thread(target=socket_process,args=(sock,arr)).start()


def socket_process(sock:socket.socket,addr):
    print("位于%s 的客户端已经连接上" % addr)
    while True:
        re_data = sock.recv(1024)

