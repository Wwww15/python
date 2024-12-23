from collections import deque

d = deque([1, 2, 3])
d.append(5)
d.appendleft(4)
print(d)

popleft = d.popleft()
print(popleft)
pop = d.pop()
print(pop)

print(d)
