import os


def thread():
    print("当前线程的pid:" % os.getpid())
    pid = os.fork()
    if pid:
        print("子进程pid：%s，父进程pid：%s" % (pid, os.getppid()))
    else:
        print("子进程pid：%s，父进程pid：%s" % (os.getpid(), os.getppid()))



