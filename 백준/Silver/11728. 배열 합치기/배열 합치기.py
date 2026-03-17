from collections import deque

n, m = map(int, input().split())

a = deque(sorted(map(int, input().split())))
b = deque(sorted(map(int, input().split())))


cnt = 0
answer = []

while len(a) > 0 and len(b) > 0:
    if a[cnt] < b[cnt]:
        answer.append(a[cnt])
        a.popleft()
    else:
        answer.append(b[cnt])
        b.popleft()

if len(a) > 0:
    for i in a:
        answer.append(i)
else:
    for i in b:
        answer.append(i)

print(*answer)