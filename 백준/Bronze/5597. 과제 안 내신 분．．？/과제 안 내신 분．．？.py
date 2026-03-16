student = [0] * 31

for i in range(28):
  n = int(input())
  student[n] = 1

for i in range(1, len(student)):
  if student[i] != 1:
    print(i)