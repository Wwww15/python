from pathlib import Path


def read_test():
    path = "test.txt"
    with open(path, 'r', encoding='utf-8') as f:
        readlines = f.readlines()
    print(readlines)


def copy_png():
    path1 = "C:\\Users\\wenzx\\Desktop\\girl1.png"
    posix_path1 = Path(path1).as_posix()
    with open(posix_path1, 'rb') as f:
        picture = f.read()
    path2 = "C:\\Users\\wenzx\\Desktop\\girl2.png"
    posix_path2 = Path(path1).as_posix()
    with open(posix_path1, 'w') as f:
        f.write(picture)


if __name__ == '__main__':
    read_test()



