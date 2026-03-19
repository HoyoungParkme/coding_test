N = int(input())
waiting = list(map(int, input().split()))

waiting.sort(reverse = True)
answer = 0

for i in range(N):
    answer += sum(waiting[i:])
print(answer)