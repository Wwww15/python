import threading
import time

sum_num = 0
lock = threading.Lock()


def add(num):
    global sum_num
    if sum_num % 2 == 0:
        sum_num = sum_num + num
    else:
        sum_num = sum_num - num


def batch_add(num):
    for item in range(100):
        add(num)
        time.sleep(1)


def batch_lock_add(num):
    for item in range(100):
        try:
            lock.acquire()
            add(num)
            time.sleep(1)
        finally:
            lock.release()


def do_thread():
    thread_one = threading.Thread(target=batch_add, args=(3,))
    thread_two = threading.Thread(target=batch_add, args=(5,))
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
    print("相加过后的总值：%d" % sum_num)


def do_lock_thread():
    thread_one = threading.Thread(target=batch_lock_add, args=(3,))
    thread_two = threading.Thread(target=batch_lock_add, args=(5,))
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()
    print("相加过后的总值：%d" % sum_num)


if __name__ == '__main__':
    do_thread()
