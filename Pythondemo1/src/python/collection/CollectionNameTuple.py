from collections import namedtuple

Student = namedtuple('Student', ['x', 'y'])

student = Student("张三", 180)

print(student.x)
print(student.y)
print(isinstance(student, tuple))
print(isinstance(student, Student))
