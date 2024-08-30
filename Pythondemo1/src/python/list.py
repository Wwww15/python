students = ['张三', '李四', '王五']
print('总的人数', len(students))
print('第一个', students[0])
print('第二个', students[1])
print('第三个', students[2])

students.append('老六')
print('最后一个人是', students[-1])

delItem = students.pop()
print('删除的元素', delItem)

students[1] = '张三三'
print('第一个', students[1])

students.append(4)
students.append(4.30)
students.append(False)
print(students)

studentTwo = ['小红', '小白']
students.append(studentTwo)
print(students)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])
