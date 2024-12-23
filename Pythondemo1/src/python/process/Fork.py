import os


def thread():
    print("当前线程的pid: %s" % os.getpid())
    pid = os.fork()
    if pid == 0:
        print("当前为子进程,pid：%s，父pid：%s" % (os.getpid(), os.getppid()))
    else:
        print("当前为父进程,pid：%s，子pid：%s" % (os.getpid(), pid))


if __name__ == '__main__':
    thread()
