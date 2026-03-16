num = [0] * 10

for i in range(10):
  num[i] = int(input()) % 42

print(len(set(num)))
