from itertools import combinations

N, M = list(map(int, input().split()))

nums = [i for i in range(1, N +1)]

for i in list(combinations(nums, M)):
    print(*i)