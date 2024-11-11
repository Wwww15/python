import struct

if __name__ == '__main__':
    # byte_arr = b'zhangsan'
    # print(byte_arr)

    math_byte = struct.pack(">I", 4294967291)
    print(math_byte)

    math = struct.unpack(">I", math_byte)
    print(math)

    math_byte_two = struct.pack(">H", 1024)
    print(math_byte_two)

    math_two = struct.unpack(">H", math_byte_two)
    print(math_two)

    # 这里是将数组的先将前4位转换成数字，后2位转换成数字
    math_three = struct.unpack(">IH", b'\xff\xff\xff\xfb\x04\x00')
    print(math_three)
