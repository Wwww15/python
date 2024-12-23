import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register("get_send_queue")
QueueManager.register("get_receive_queue")

manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
manager.connect()
send_queue = manager.get_send_queue()
receive_queue = manager.get_receive_queue()

while True:
    try:
        msg = send_queue.get(timeout=10)
        print("worker receice num: %d" % msg)
        receive_queue.put(msg * msg)
    except queue.Empty:
        print("queue is empty!")
        break

print("worker end !")
