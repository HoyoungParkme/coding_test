import sys

T = int(input())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()
    b.sort()

    cnt = 0
    j = 0

    for i in range(n):
        while j < m and a[i] > b[j]:
            j += 1
        cnt += j

    print(cnt)