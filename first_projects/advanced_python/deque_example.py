import collections

de = collections.deque([1, 2, 3])
de.append(4)
de.appendleft(20)
print(de)  # deque([20, 1, 2, 3, 4])

de.pop()
de.popleft()
print(de)  # deque([1, 2, 3])
