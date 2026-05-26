from itertools import combinations

def solution(nums):
    answer = 0
    take = len(nums)//2
    a = list(set(nums))
    
    if take > len(a):
        answer = len(a)
    else:
        answer = take
    
    return answer