import os, threading
import time


def do_task():
    print("current thread name : %s start" % threading.current_thread().name)
    for x in range(5):
        print("current thread name : %s ,do >>> %d" % (threading.current_thread().name, x))
        time.sleep(2)


def start_thread():
    thread_one = threading.Thread(target=do_task, name="thread_one")
    thread_one.start()
    thread_one.join()
    print("Thead ：%s is over" % thread_one.name)


if __name__ == '__main__':
    start_thread()