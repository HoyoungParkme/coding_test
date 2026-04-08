N = input()

tmp = ""
cnt = 0
flag = False

for i in range(len(N)):
    if N[i] == 'X':
        cnt += 1
        if cnt == 4:
            tmp += 'AAAA'
            cnt = 0
    else:
        if cnt == 1 or cnt ==3:
            flag = True
            break 
        elif cnt == 2:
            tmp += 'BB'
            cnt = 0
        
        tmp += '.'
        cnt = 0

if cnt == 1 or cnt == 3:
    flag = True
elif cnt == 2:
    tmp += 'BB'

if flag:
    print(-1)
else:
    print(tmp)
