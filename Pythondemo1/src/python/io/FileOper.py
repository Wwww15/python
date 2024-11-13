import os
import shutil
from pathlib import Path

if __name__ == '__main__':
    # print(os.uname())
    print(os.name)
    print(os.environ)
    print(type(os.environ))
    # 获取当前py脚本执行的绝对路径
    abspath = os.path.abspath(".")
    print(abspath)
    # 安全的拼接路径
    new_path = os.path.join(abspath, "tmp")
    if not os.path.exists(new_path):
        # 创建文件夹
        os.mkdir(new_path)
    else:
        # 删除文件夹
        os.rmdir(new_path)

    path = "test.txt"
    absolute_path = Path(path).absolute()
    # 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
    split_arr = os.path.split(absolute_path)
    print(split_arr)
    # 可以直接让你得到文件扩展名
    splitext_arr = os.path.splitext(absolute_path)
    print(splitext_arr)
    # 重命名
    # os.rename(path, 'test1.txt')
    # 复制
    shutil.copy("test1.txt", "test.txt")
    # 过滤
    filter = [x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
    print(filter)

