N = int(input())
level = [int(input()) for _ in range(N)]
answer = 0

for i in range(N - 1, 0, -1):
    if level[i] <= level[i-1]:
        diff = level[i-1] - (level[i] - 1)
        answer += diff
        level[i-1] = level[i] - 1

print(answer)