A, B, C, M = list(map(int, input().split()))

work = 0
fuck = 0

for _ in range(24):
    if fuck + A > M:
        fuck = max(0, fuck - C)
    else:
        work += B
        fuck += A

if A > M:
    print(0)
else:
    print(work)
