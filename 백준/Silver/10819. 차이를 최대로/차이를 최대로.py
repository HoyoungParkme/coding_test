from itertools import combinations, permutations

N = int(input())
pocket = list(map(int, input().split()))

answer = 0
for i in permutations(pocket, N):
    diff = 0
    for j in range(0, len(i)-1):
        diff += abs(i[j] - i[j+1])

    if diff > answer:
        answer = diff

print(answer)

