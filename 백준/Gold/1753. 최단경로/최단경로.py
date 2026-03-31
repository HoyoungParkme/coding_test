# from queue import PriorityQueue
import heapq
import sys
input = sys.stdin.readline

V, E = list(map(int, input().split()))
K = int(input()) - 1

adj = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    adj[u - 1].append((v - 1, w))

dist = [1e9] * V
dist[K] = 0
pq = []
heapq.heappush(pq, (0,K))
# pq = PriorityQueue()
# pq.put((0,K)) # 초기 K값은 시작이 0이니깐 이상태로 튜플에 넣음

# while pq.qsize() != 0:
#     d, u = pq.get()
#
#     if d != dist[u]:
#         continue
#
#     for v, w in adj[u]:
#         if dist[v] > dist[u] + w:
#             dist[v] = dist[u] + w
#             pq.put((dist[v], v))

while pq:
    d, u = heapq.heappop(pq)

    if d != dist[u]:
        continue

    for v, w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

for i in range(V):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])