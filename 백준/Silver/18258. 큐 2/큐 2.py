import sys
from collections import deque

N = int(input())
q = deque([])

for i in range(N):
    command = sys.stdin.readline()
    command = command.split()

    if command[0] == 'push':
        q.append(command[1])

    if command[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)

    if command[0] == 'size':
        print(len(q))

    if command[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    if command[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)

    if command[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)




