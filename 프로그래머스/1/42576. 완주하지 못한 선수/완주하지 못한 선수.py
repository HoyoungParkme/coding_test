from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    diff = p-c
    return next(iter(diff))