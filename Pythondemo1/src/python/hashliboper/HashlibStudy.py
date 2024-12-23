import hashlib


def md5_encode(data: str):
    md5 = hashlib.md5()
    md5.update(data.encode("utf-8"))
    return md5.hexdigest()


def md5_seperate_encode(*datas):
    if not datas or len(datas) <= 0:
        raise Exception("请至少传入一个参数")
    md5 = hashlib.md5()
    for data in datas:
        md5.update(data.encode("utf-8"))
    return md5.hexdigest()


def sha1_encode(data: str):
    sha1 = hashlib.sha1()
    sha1.update(data.encode("utf-8"))
    return sha1.hexdigest()


def sha1_seperate_encode(*datas):
    if not datas or len(datas) <= 0:
        raise Exception("请至少传入一个参数")
    sha1 = hashlib.sha1()
    for data in datas:
        sha1.update(data.encode("utf-8"))
    return sha1.hexdigest()


if __name__ == '__main__':
    print(md5_encode("hello！你是张三吧！"))
    print(md5_seperate_encode("hello！", "你是张三吧！"))

    print(sha1_encode("sha1加密！你好啊！"))
    print(sha1_seperate_encode("sha1加密！", "你好啊！"))
