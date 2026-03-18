N, M = map(int, input().split())
pocket = list(map(int, input().split()))

left = 0
right = 0
pocket_sum = 0
answer = 0

while True:
    if pocket_sum >= M:
        if pocket_sum == M:
            answer += 1
        pocket_sum -= pocket[left]
        left += 1
    elif right == N:
        break
    else:
        pocket_sum += pocket[right]
        right += 1

print(answer)


