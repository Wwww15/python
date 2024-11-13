import itertools, time


def iter_count():
    count = itertools.count(-1)
    for i in count:
        print(i)
        time.sleep(2)


def iter_cycle():
    cycle = itertools.cycle("你猜我是谁")
    for i in cycle:
        print(i)
        time.sleep(2)


def iter_repeat():
    repeat = itertools.repeat("你TM谁啊")
    for i in repeat:
        print(i)
        time.sleep(2)


def item_takewhile():
    count = itertools.count(0)
    takewhile_count = itertools.takewhile(lambda x: x <= 10, count)
    for i in takewhile_count:
        print(i)


def iter_chain():
    chain = itertools.chain("张三", "李四")
    # cycle = itertools.cycle(chain)
    for i in chain:
        print(i)


"""
相邻元素分组
"""


def iter_groupby():
    groupby = itertools.groupby("AAAAccAaasdadasadadsa123131asdadaaodkapalskjd张三")
    for key, arr in groupby:
        print(key, list(arr))


if __name__ == "__main__":
    # iter_count()
    # item_takewhile()
    iter_chain()
    # iter_groupby()
