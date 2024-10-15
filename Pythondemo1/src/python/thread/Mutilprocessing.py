import os, time, random
from multiprocessing import Process, Pool


def do_extra(name):
    print("%s 开始在线路 %s 搞事儿啦，主线路: %s！" % (name, os.getpid(), os.getppid()))


def mutilt_process():
    name = "小明"
    process = Process(target=do_extra, args=(name,))
    print("开始在线路 %s 上课啦！" % os.getpid())
    process.start()
    process.join()
    print(" %s 搞事儿完了" % name)


def do_pool_process(index):
    print("子线程pid: %s，第 %s 孩子，开始执行啦" % (os.getpid(), index))
    sleep_time = 1 + random.random() * 3
    start = time.time()
    time.sleep(sleep_time)
    end = time.time()
    print("子线程pid: %s，第 %s 孩子，执行完啦，执行时间：%d" % (os.getpid(), index, end - start))

def pool_process():
    pool = Pool()
    print("父线程pid: %s" % os.getpid())
    print("当前cpu核心数: %s" % os.cpu_count())
    for index in range(20):
            pool.apply_async(do_pool_process, args=(index,))

    pool.close()
    pool.join()
    print("所有的子线程都执行完啦！")


if __name__ == '__main__':
    # mutilt_process()
    pool_process()

