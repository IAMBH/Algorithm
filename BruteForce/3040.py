# 3040 백설공주와 일곱 난쟁이
import itertools

dwarf = []
for i in range(9):
    dwarf.append(int(input()))

cases = list(itertools.combinations(dwarf, 7))

for case in cases:
    if sum(case) == 100:
        for c in case:
            print(c)