import threading
from collections import ChainMap
import os, argparse




def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-name", "--name")
    parser.add_argument("-pwd", "--password")
    args = parser.parse_args()
    print(args)
    return {k: v for k, v in vars(args).items() if v}


def default_args():
    return {"name": "zhangsan", "password": "123456"}


chain_map = ChainMap(get_args(), os.environ, default_args())

print("name：%s" % chain_map.get("name"))
print("password：%s" % chain_map.get("password"))
