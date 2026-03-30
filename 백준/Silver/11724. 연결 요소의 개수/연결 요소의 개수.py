import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
adj = [[] for i in range(N)]

for _ in range(M):
    u, v = list(map(int, input().split()))
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

visit = [False] * N
cnt = 0

for i in range(N):
    if visit[i]:
        continue

    cnt += 1
    queue = deque([i])
    visit[i] = True

    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True

print(cnt)