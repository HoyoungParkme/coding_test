from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))


cnt = 0
for i in range(N):
    tmp = list(combinations(nums, i+1))

    for i in range(len(tmp)):
        if sum(tmp[i]) == S:
            cnt += 1
        
print(cnt)        