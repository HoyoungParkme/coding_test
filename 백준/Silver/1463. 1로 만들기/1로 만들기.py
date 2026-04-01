N = int(input())

a = [0] * (N + 1)
a[0] = 1

for i in range(2, N+1):
    # 1을 뺀거 -> 1빼면 이전에 걸로 돌아가는거니깐 -> ex) a[2] - 1 = a[1]
    # +1을 해주는건 몇번 했는지 체크하는데 돌아간거 한번 체크
    a[i] = a[i - 1] + 1

    if i % 3 ==0:
        a[i] = min(a[i], a[i//3] + 1)

    if i % 2 == 0:
        a[i] = min(a[i], a[i//2] +1 )

print(a[N])
