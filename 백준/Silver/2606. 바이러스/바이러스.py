import sys
N = int(input())
M = int(input())

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

check= [0] * N
check[0] = 1

while True:
    new = False
    for i in range(N):
        if check[i] == 0:
            continue

        for j in adj[i]:
            if check[j] == 0:
                check[j] = 1

                new = True
    if not new:
        break

answer = 0
for i in range(1,N):
    if check[i] == 1:
        answer += 1

print(answer)
