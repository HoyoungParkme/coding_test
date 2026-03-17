import sys

for _ in range(int(input())):
    arr = []

    for _ in range(int(input())):
        a, b = map(int, sys.stdin.readline().split())
        arr.append([a,b])

    arr.sort()
    cnt = 1
    standard = arr[0][1]

    for i in range(1, len(arr)):
        if arr[i][1] < standard:
            cnt += 1
            standard = arr[i][1]

    print(cnt)




