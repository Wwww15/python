import  psutil




def cpu_info():
    logic_count = psutil.cpu_count()
    print(logic_count)
    physics_count = psutil.cpu_count(logical=False)
    print(physics_count)
    times = psutil.cpu_times()
    print(times)

def cpu_use_info():
    percent = psutil.cpu_percent(interval=1, percpu=True)
    print(percent)


def memory_info():
    v_memory = psutil.virtual_memory()
    s_memory = psutil.swap_memory()
    print(v_memory)
    print(s_memory)


def dist_info():
    d_partitions = psutil.disk_partitions()
    d_usage = psutil.disk_usage("/")
    d_io_counters = psutil.disk_io_counters()
    print(d_partitions)
    print(d_usage)
    print(d_io_counters)


def net_info():
    connections_info = psutil.net_connections()
    print(connections_info)

def process_info():
    pids = psutil.pids()
    print(pids)
    process = psutil.Process(2332)
    print(process)
    print(process.parent())
    print(process.num_threads())
    print(process.threads())


def sys_info():
    users = psutil.users()
    print(users)


if __name__ == "__main__":
    # cpu_info()
    # for index in range(10):
    #     cpu_use_info()
    # memory_info()
    # dist_info()
    # net_info()
    # process_info()
    sys_info()