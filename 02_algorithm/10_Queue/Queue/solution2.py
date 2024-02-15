from collections import deque
# double ended queue

q = deque()
q.append('a')
q.append('b')
print(q)

q.appendleft('c') # insert
print(q)

print(q.pop())
print(q.popleft())