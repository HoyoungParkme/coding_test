import math
N = int(input())

# 1개 체크
if int(math.sqrt(N))**2 == N:
    print(1)
    exit()

# 2개 체크
for i in range(1, int(math.sqrt(N)) + 1):
    if int(math.sqrt(N - i*i))**2 == N - i*i:
        print(2)
        exit()

# 3개 or 4개 체크 (Legendre)
n = N
while n % 4 == 0:
    n //= 4
if n % 8 == 7:
    print(4)
else:
    print(3)