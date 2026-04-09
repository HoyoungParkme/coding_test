from collections import deque
N, K = map(int, input().split())

people = [i for i in range(1, N+1)]    

q = deque(people)

answer = []

for i in range(N):
    q.rotate(-(K - 1))
    answer.append(q.popleft())

print('<' + ', '.join(map(str, answer)) + '>')