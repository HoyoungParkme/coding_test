import math

def solution(progresses, speeds):
    finish = []
    rank = []
    
    for p, s in zip(progresses, speeds):
        result = math.ceil((100-p)/s)
        finish.append(result)
    
    now = finish[0]
    cnt = 1
    
    for day in finish[1:]:
        if day <= now:
            cnt += 1
        else:
            rank.append(cnt)
            cnt = 1
            now = day
            
    rank.append(cnt)
            
    return rank