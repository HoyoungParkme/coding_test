left = []

while True:
  tmp = input()
  
  if tmp == '.':
    break

  flag = True
  left = []

  for j in tmp:
    if j in [']', ')'] and len(left) == 0:
      flag = False
      break

    if j == ']':
      if left[-1] == '[':
        left.pop()
      else:
        flag = False
        break

    elif j == ')':
      if left[-1] == '(':
        left.pop()
      else:
        flag = False
        break

    elif j in ['[', '(']:
      left.append(j)

  if flag == False or len(left) > 0:
    print('no')
  else:
    print('yes')