import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visit = [False] * N
parent = [-1] * N

def dfs(u):
    visit[u] = True
    for v in adj[u]:
        if not visit[v]:
            parent[v] = u
            dfs(v)

dfs(0)

for i in range(1, N):
    print(parent[i] + 1)