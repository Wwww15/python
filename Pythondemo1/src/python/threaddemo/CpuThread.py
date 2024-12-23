import multiprocessing
import threading


def do_loop():
    sum = 0
    while (True):
        sum = sum + 1


def cpu_loop():
    for index in range(multiprocessing.cpu_count()):
        thread = threading.Thread(target=do_loop)
        thread.start()


if __name__ == '__main__':
    cpu_loop()
