from iooper import StringIO


if __name__ == '__main__':
    string_io = StringIO("1.Mybatis的二级缓存原理\n2.Mybatis的动态代理原理和过程")
    while True:
        readline = string_io.readline()
        if readline:
            print(readline)
        else:
            break
