import hmac

key = "123456"


def hmac_encode(data: str):
    hmac_new = hmac.new(key.encode("utf-8"), data.encode("utf-8"), "md5")
    return hmac_new.hexdigest()


def hmac_sperate_encode(*datas):
    hmac_new = hmac.new(key.encode("utf-8"), b'', "md5")
    for data in datas:
        hmac_new.update(data.encode("utf-8"))
    return hmac_new.hexdigest()


if __name__ == "__main__":
    print(hmac_encode("hmac！你来啦！"))
    print(hmac_sperate_encode("hmac！", "你来啦！"))
