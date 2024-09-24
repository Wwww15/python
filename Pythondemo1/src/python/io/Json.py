import json

# json
temp_dict = dict(name="John", age=25)
json_data = json.dumps(temp_dict)
print(json_data)

with open("test_json.json", 'w') as f:
    json.dump(json_data, f)

with open('test_json.json', 'r') as f:
    content = json.load(f)
    print(content)


class Student(object):
    __slot__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


def to_stu(item,item2):
    return Student(item["name"], item["age"])


student = Student("zhangsan", 20)
dumps = json.dumps(student, default=lambda obj: obj.__dict__)
print(dumps)

with open("test_json.json", "r") as f:
    result = json.load(f, object_hook=to_stu)
    print(result)
    print(type(result))
