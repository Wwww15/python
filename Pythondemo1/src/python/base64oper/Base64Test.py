import base64


def base64_encode(data):
    return base64.b64encode(data)


def base64_decode(data):
    return base64.b64decode(data)


def safe_base64_decode(s):
    a = len(s) % 4
    if a == 0:
        return base64_decode(s)
    else:
        s += '=' * (4 - a)
        return base64_decode(s)


if __name__ == '__main__':
    # 测试:
    assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
    print('ok')
