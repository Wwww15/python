# 字符串方法
name = "kevin smith"
print(name.title())
print(name.upper())
print(name.lower())

# 字符串+变量
first_name = "张"
last_name = "三"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello,{full_name.title()} f形式!"
print(message)
message = "{} {} format形式！ ".format(first_name, last_name);
print(message)

# 字符串中的制表符、换行符、空白
print("Python")
print("\tPython")
print("Subject:\nscience\nmath\nhistory")

# 去除空白
# 尾部 rstrip
favorite = "Python "
print(len(favorite))
print(len(favorite.rstrip()))
print(len(favorite))
favorite = favorite.rstrip()
print(len(favorite))

# 前面 lstrip
favorite = " Python "
print(len(favorite))
print(len(favorite.lstrip()))

# 两边 strip
print(len(favorite.strip()))

# 符号
message = "One of Python's strengths is its diverse community."
print(message)

message = 'One of Pythons strengths is its diverse community.'
print(message)

# 测试
message = 'Albert Einstein once said, “A person who never made a mistake nevertried anything new.”'
print(message)
famous_person = "Albert Einstein"
newMessage = f'{famous_person} once said, “A person who never made a mistake nevertried anything new.”'
print(newMessage)
famous_person = " Albert Einstein "
newMessage = f'{famous_person.lstrip()} once said, “A person who never made a mistake nevertried anything new.”'
print(newMessage)

txt = "apple/banana/cherry/apple/banana/cherry"

x = txt.rsplit("/", 1)

print(x[0])
