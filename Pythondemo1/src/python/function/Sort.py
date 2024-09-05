lists = [-1, 1, 0, -9, 10]
print(sorted(lists))

lists1 = [-9, 10, 12, -10, 0]
print(sorted(lists1, key=abs))

str1 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(str1))
print(sorted(str1, key=str.lower))
print(sorted(str1, key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)
