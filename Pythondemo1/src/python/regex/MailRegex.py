import re


def is_valid_email(addr):
    regex = r'^[\w\.]+@\w+\.com$'
    if re.match(regex, addr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
