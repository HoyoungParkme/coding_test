cnt = int(input())
money = []

for i in range(cnt):
  n = int(input())
  if n == 0:
    money.pop()
  else:
    money.append(n)

print(sum(money))