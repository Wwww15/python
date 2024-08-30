# 条件匹配
score = 90
match score:
    case i if i >= 90:
        print('A')
    case i if i >= 80:
        print('B')
    case i if i >= 70:
        print('C')
    case i if i >= 60:
        print('D')
    case _:
        print("E")

# 匹配多个值
like = '家里蹲'

match like:
    case '排球' | '篮球' | '乒乓球' | '足球':
        print('玩球高手啊，你是')
    case '高尔夫':
        print('土豪你好')
    case '家里蹲':
        print('土肥圆')

# 列表匹配

likes = ['排球', '桌球', '篮球', '乒乓球']

match likes:
    case ['排球']:
        print('我俩都喜欢排球呀')
    case ['排球', other1, other2]:
        print('除了排球，你还喜欢 %s 和 %s' % (other1, other2))
    case ['排球', '桌球', '篮球']:
        print('我俩爱好一模一样')
    case _:
        print('滚吧，你跟我玩不到一块')
