import sys
input = sys.stdin.readline

N = int(input())
level = list(map(int, input().split()))
Q = int(input())

arr = [0] * N
for i in range(N - 1):
    if level[i] > level[i+1]:
        arr[i] = 1

psum = [0] * (N+1)
for i in range(N-1):
    if i == 0:
        psum[i] = arr[i]
    else:
            psum[i] = psum[i-1] + arr[i]

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    if x == y:
        print(0)
        continue

    ans = psum[y-1]
    if x > 0:
        ans -= psum[x-1] 

    print(ans)
        
    
