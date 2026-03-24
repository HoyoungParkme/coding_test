from collections import deque

N = int(input())
M = deque([])

for _ in range(N):
    M.append(int(input()))


tmp = M.popleft()
answer = 0
while M:
    max_value = max(M)
    max_index = M.index(max_value)

    if max_value < tmp:
        break

    M[max_index] = max_value - 1
    answer += 1
    tmp += 1

print(answer)