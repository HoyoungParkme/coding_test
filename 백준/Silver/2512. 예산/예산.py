num = int(input())
local = list(map(int, input().split()))
money = int(input())

start = 0
end = max(local)
answer = 0

while start <= end:
    mid = (start + end)//2

    total = 0
    for i in local:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= money:
        answer = mid
        start = mid + 1

    else:
        end = mid - 1

print(answer)



