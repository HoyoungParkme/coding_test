def solution(priorities, location):
    q = []
    
    for i in range(len(priorities)):
        q.append([priorities[i],i])
    
    cnt = 0
    
    while q:
        tmp = q.pop(0)
        
        if tmp[0] < max([n[0] for n in q], default=0):
            q.append(tmp)
        else:
            cnt += 1
            if tmp[1] == location:
                return cnt
            
    return cnt