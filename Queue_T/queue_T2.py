from collections import deque

q = deque([1, 2, 3, 4, 5], 5)
q.append(6)
print(q.popleft())

def tail(n):  # like the tail function in linux, with it can also the last 5 lines be printed.
    q = deque(n, 3)
    return q

for i in tail('fjasdifjaosd'):
    print(i)
