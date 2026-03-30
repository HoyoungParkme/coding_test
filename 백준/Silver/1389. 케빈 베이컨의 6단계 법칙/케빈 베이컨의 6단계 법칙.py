import sys
from collections import deque

input = sys.stdin.readline
N, M = list(map(int, input().split()))
adj = [[] for _ in range(N)]

for _ in range(M):
    u, v = list(map(int, input().split()))
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

min_kevin = 1e9
min_person = -1

for i in range(N):
    visit = [False] * N
    visit[i] = True
    dist = [-1] * N
    dist[i] = 0
    queue = deque([i])

    while len(queue) != 0:
        u = queue.popleft()

        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True
                dist[v] = dist[u] + 1
    kevin = sum(dist)

    if kevin < min_kevin:
        min_kevin = kevin
        min_person = i + 1

print(min_person)

