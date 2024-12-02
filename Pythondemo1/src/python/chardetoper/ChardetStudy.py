import chardet

def study_one():
    byte_a = b'132131'
    result = chardet.detect(byte_a)
    print(result)

def study_two():
    str_b = "你猜"
    result = chardet.detect(str_b.encode("gb2312"))
    print(result)


def study_three():
    str_c = "最新の主要ニュース"
    result = chardet.detect(str_c.encode("euc-jp"))
    print(result)


if __name__ == "__main__":
    # study_one()
    study_two()
    # study_three()