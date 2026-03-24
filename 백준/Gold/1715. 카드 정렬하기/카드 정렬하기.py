from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()

for _ in range(N):
    card = int(input())
    pq.put(card)

answer = 0
while pq.qsize() > 1:
    min_value_1 = pq.get()
    min_value_2 = pq.get()
    pq.put(min_value_1 + min_value_2)
    answer += min_value_1 + min_value_2

print(answer)