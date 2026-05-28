def solution(s):
    check = []
    
    for i in s:
        if i == "(":
            check.append(i)
        else:
            if len(check) == 0:
                return False
            check.pop()
        
    return len(check) == 0