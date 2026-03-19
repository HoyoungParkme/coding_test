N, K, B = map(int, input().split())
broken = []

for i in range(B):
    broken.append(int(input()))

# 고장난 신호등
tmp = [0] * N
for i in broken:
    tmp[i-1] = 1

# 누적합
p = [0] * N
p[0] = tmp[0]
for i in range(1, N):
    p[i] = p[i-1] + tmp[i]


answer = p[K-1]
for i in range(K, N):
    answer = min(answer, p[i] - p[i-K])

print(answer)