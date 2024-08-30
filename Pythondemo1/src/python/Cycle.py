# 输出集合中的元素
likes = ['小红', '小青', '小紫', '小兰']
for like in likes:
    print(like)

# 求和
maths = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for math in maths:
    sum += math
print(sum)

# 利用range 求和
sum1 = 0
for item in range(10):
    sum1 += item
print(sum1)

# while 求和
start = 0
end = 10
sum2 = 0
while start < end:
    sum2 += start
    start += 1
print(sum2)

# 打印格式化名称
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,{0}'.format(name))

# break
start = 0
end = 10
sum3 = 0
while start< end:
    if start == 5:
        print('碰到幸运数字{0}，退出'.format(start))
        break
    sum3 += start
    start += 1
print(sum3)
