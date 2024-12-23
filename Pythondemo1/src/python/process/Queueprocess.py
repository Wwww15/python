import os
import time
from multiprocessing import Process, Queue


def write(queue: Queue):
    print("写入数据的线程pid：%s " % os.getpid())
    queue.put("你好，在吗？")
    time.sleep(1)
    queue.put("喂，你在干嘛？")
    time.sleep(1)
    queue.put("我在你家楼下等你")


def read(queue: Queue):
    print("读取数据的线程pid：%s " % os.getpid())
    while (True):
        msg = queue.get(True)
        print("读取到的数据：%s" % msg)


if __name__ == "__main__":
    print("当前主线程pid：%s" % os.getpid())
    queue = Queue()
    write_process = Process(target=write, args=(queue,))
    read_process = Process(target=read, args=(queue,))
    write_process.start()
    read_process.start()
    write_process.join()
    read_process.terminate()
    print("主线程结束")
