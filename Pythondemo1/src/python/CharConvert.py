print(chr(89))

print(ord('中'))

baseByte = '中国'.encode('unicode_escape')
print(baseByte)

print('\u4e2d\u6587')

baseByte = '中国'.encode('utf-8')
print(baseByte)

decodeByte = b'\xe4\xb8\xad\xe1'
print(decodeByte.decode('utf-8', 'ignore'))

placeHolder = 'hello,%s' % '张三' + ',今年我%d岁了' % 18 + ',你呢?'
print(placeHolder)

print('%2d-%02d' % (3.14, 1000.033))
print('%.2f' % 3.1415926)
