from typing import Deque

import collections

a = collections.deque([i for i in range(1, 10, 2)])
print(a)
a.rotate(-1)
print('deque rotate(-1)', list(a))

a.append(23)
print('deque append(23)', a)

a.appendleft(32)
print('deque appendleft(32)', a)

a.pop()
print('deque pop()', a)

a.popleft()
print('deque popleft()', a)


b = collections.deque([i for i in range(1, 10, 2)])
c = collections.deque([i for i in range(1, 10, 2)])

b.append('ef')
print("deque append('ef')", b)

c.extend('ef')
print("deque extend('ef')", c)