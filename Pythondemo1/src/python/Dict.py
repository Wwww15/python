scoreDict = {'张三': 98, '李四': 90, '王五': 60, '校长': 98}
print(scoreDict['张三'])

scoreDict['王五'] = 54
print(scoreDict['王五'])
print('王麻子' in scoreDict)
print('王五' in scoreDict)


print(scoreDict.get('王麻子'))
print(scoreDict.get('王五'))


print(scoreDict.pop("王五"))
print("王五" in scoreDict)
print(scoreDict)