N = int(input())

left = 0
right = 2**32

answer = -1
while left <= right:
    mid = (left + right) // 2
    if mid ** 2 < N:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1
print(answer)