from queue import PriorityQueue

N, M, X = list(map(int, input().split()))
X -= 1

adj = [[] for _ in range(N)]
r_adj = [[] for _ in range(N)]
for _ in range(M):
    start, end, time = list(map(int, input().split()))
    adj[start - 1].append((end-1, time))
    r_adj[end - 1].append((start-1, time))

dist = [1e9] * N
dist[X] = 0
pq = PriorityQueue()
pq.put((0,X))

while pq.qsize() != 0:
    d, u = pq.get()
    if d != dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((dist[v], v))


r_dist = [1e9] * N
r_dist[X] = 0
pq = PriorityQueue()
pq.put((0,X))

while pq.qsize() != 0:
    d, u = pq.get()
    if d != r_dist[u]:
        continue
    for v, w in r_adj[u]:
        if r_dist[v] > r_dist[u] + w:
            r_dist[v] = r_dist[u] + w
            pq.put((r_dist[v], v))

max_dist = 0
for i in range(N):
    if max_dist < dist[i] + r_dist[i]:
        max_dist = dist[i] + r_dist[i]
print(max_dist)

