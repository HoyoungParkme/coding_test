s = [-1] * 26
s2 = str(input())
for i in range(len(s2)):
  n = ord(s2[i]) - ord('a')

  if s[n] == -1:
    s[n] = i

print(*s)
