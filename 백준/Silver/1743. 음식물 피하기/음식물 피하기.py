from collections import deque

N, M, K = map(int, input().split())

points = set()
for _ in range(K):
    a,b = map(int, input().split())
    points.add((a,b))

visit = set()
move = [(0,1), (0,-1), (1,0), (-1,0)]
max_num = 0

def bfs(start):
    q = deque([start])
    visit.add(start)
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if (nx, ny) in points and (nx, ny) not in visit:
                q.append((nx, ny))
                visit.add((nx, ny))
                cnt += 1

    return cnt


for i in points:
    if i not in visit:
        max_num = max(max_num, bfs(i))

print(max_num)


