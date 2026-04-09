N, M = list(map(int, input().split()))
tree = list(map(int, input().split()))

lo, hi = 0, max(tree)

def check(n):
    tmp = 0
    for i in tree:
        if i > n:
            tmp += (i - n)
    return tmp >= M

answer = 0
while lo <= hi:
    mid = (lo + hi) // 2

    if check(mid):
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)
    
