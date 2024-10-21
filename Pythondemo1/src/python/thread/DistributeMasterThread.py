import queue, random, time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 发送消息
def send_msg(send_queue: queue.Queue):
    for i in range(20):
        num = random.randint(100, 100000)
        print("master math: %d" % num)
        send_queue.put(num)


# 接受消息
def get_msg(receive_queue: queue.Queue):
    n = 1
    while True:
        # if n > 3:
        #     break
        result = receive_queue.get(timeout=1000)
        # if not result:
        #     time.sleep(n * 2)
        #     n += 1
        print("master receive num: %d" % result)


# 发送队列
def send_queue():
    send_queue = queue.Queue()
    return send_queue

    # 接受队列


def receive_queue():
    receive_queue = queue.Queue()
    return receive_queue


def master_thread():
    # 注册队列
    QueueManager.register("get_send_queue", callable=send_queue)
    QueueManager.register("get_receive_queue", callable=receive_queue)
    # 绑定端口
    manager = QueueManager(address=("127.0.0.1", 5000), authkey=b"abc")
    # 启动queue
    manager.start()
    send = manager.get_send_queue()
    receive = manager.get_receive_queue()
    # 获取对应的队列对象
    send_msg(send)
    # 获取对应的队列对象
    get_msg(receive)
    manager.shutdown()
    print("master task end！")


if __name__ == '__main__':
    master_thread()
