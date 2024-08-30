names = {1, 2, 3, 4, 1, 1, 2, 5}
print(names)

# 添加
names.add(6)
names.add('张三')
print(names)

# 移除
names.remove(1)
print(names)

# 交集

names2 = {1, 2, 0, 9, '张三'}
print(names & names2)
