n = list(map(int, input().split()))
play = list(map(int, input().split()))

N = n[0]
blue = n[1]

start = max(play)
end = sum(play)
answer = 0

while start <= end:
    tmp = 0
    cnt = 1
    mid = (start + end)//2

    for i in play:
        if tmp + i <= mid:
            tmp += i
        else:
            cnt += 1
            tmp = i

    if cnt > blue:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)