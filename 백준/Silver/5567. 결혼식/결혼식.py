N = int(input())
M = int(input())

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

friend = [0] * N
for i in adj[0]:
    friend[i] = 1

friend_friend = [0] * N
for i in range(N):
    if friend[i] == 0:
        continue

    for j in adj[i]:
        if j!=0 and friend[j]==0: #이미 친구 중복 제거
            friend_friend[j] = 1

print(sum(friend) + sum(friend_friend))

