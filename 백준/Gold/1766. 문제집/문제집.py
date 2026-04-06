from queue import PriorityQueue

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N)]
need_learn = [0] * N

for i in range(M):
    a,b = list(map(int, input().split()))
    adj[a - 1].append(b-1)
    need_learn[b - 1] += 1

# 위상 정렬
pq = PriorityQueue() # 수강 가능한 목록
for i in range(N):
    if need_learn[i] == 0:
        pq.put(i)

learn = []
while pq.qsize() != 0:
    u = pq.get()
    learn.append(u)

    for v in adj[u]:
        need_learn[v] -= 1
        if need_learn[v] == 0:
            pq.put(v)

for i in range(N):
    print(learn[i] + 1, end=" ")
