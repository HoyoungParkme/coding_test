import sys

N = int(input())

for i in range(N):
    n, m = map(int,sys.stdin.readline().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    cnt, start_a, start_b  = 0, 0, 0

    while start_a < n:
        if start_b == m:
            cnt += start_b
            start_a +=1
        else:
            if a[start_a] > b[start_b]:
                start_b += 1
            else:
                cnt += start_b
                start_a += 1
    print(cnt)





