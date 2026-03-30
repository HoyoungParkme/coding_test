import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

visit = [False] * N

def dfs(node):
    visit[node] = True
    for n in adj[node]:
        if not visit[n]:
            dfs(n)


dfs(0)
cnt = 0
for i in visit:
    if i:
        cnt +=1

print(cnt - 1)