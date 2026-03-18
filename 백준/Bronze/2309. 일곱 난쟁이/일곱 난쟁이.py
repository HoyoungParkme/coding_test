from itertools import combinations

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))



for i in list(combinations(dwarf,7)):
    if sum(i) == 100:
        print(*sorted(i), sep='\n')
        break
