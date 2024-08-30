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

print('%4d-%02d' % (4111111, 1))
print('%.2f' % 3)

helloWords = '我叫张三 {0}'.format(',今年19岁')
print(helloWords)

percent = '女生占全班的 %d %%' % 20
print(percent)

grown = (85-72)/72*100
print('小明今年的成绩提升了 {0:.1f}%'.format(grown))
print('小明今年的成绩提升了 %.1f%%' % grown)