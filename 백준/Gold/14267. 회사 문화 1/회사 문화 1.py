N, C = map(int, input().split())
parent = list(map(int, input().split()))

for i in range(1,N):
    parent[i] -= 1

good = [0] * N
for i in range(C):
    a, b = map(int, input().split())
    good[a-1] += b

total = [0] * N
for i in range(1, N):
    total[i] += good[i] + total[parent[i]]

print(*total)
