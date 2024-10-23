import re


def name_of_email(addr):
    regex = r'(<([\w\s]+)>)?[\w\s]+@[\w\s]+(\.com|\.org)'
    re_compile = re.compile(regex)
    match = re_compile.match(addr)
    if match:
        group_first = match.group(1)
        print(group_first)
        return str(group_first)
    else:
        return None


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
