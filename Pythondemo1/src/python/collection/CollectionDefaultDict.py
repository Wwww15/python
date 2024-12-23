from collections import defaultdict

d = defaultdict(lambda: "这是默认值")

d["张三"] = "完美"
d["李四"] = "优秀"
val1 = d['张三']
print(val1)
val2 = d['王麻子']
print(val2)
