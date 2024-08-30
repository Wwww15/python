def trim(s):
    start = 0
    end = len(s) - 1
    startIndex = None
    endIndex = None
    while start <= end:
        if s[start] != ' ' and startIndex is None:
            startIndex = start
        else:
            start += 1
        if s[end] != ' ' and endIndex is None:
            endIndex = end
        else:
            end -= 1
    if startIndex is None or endIndex is None:
        return ''
    return s[startIndex:endIndex + 1]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
elif trim('  A  ') != 'A':
    print('测试失败!')
else:
    print('测试成功!')
