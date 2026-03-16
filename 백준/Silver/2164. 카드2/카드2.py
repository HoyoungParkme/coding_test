import sys
from collections import deque

N = int(input())
q = deque([])
cnt = 0

for i in range(1,N+1):
    q.append(i)

while len(q) > 1:
    cnt += 1
    if cnt % 2 == 1:
        q.popleft()
    else:
        q.append(q[0])
        q.popleft()
print(*q)





