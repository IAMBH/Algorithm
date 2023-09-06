# 2231
n = int(input())

const_li = []

for i in range(1,n+1):
    constructor = i
    digit = [int(str(i)[idx]) for idx in range(len(str(i)))]
    for d in digit:
        constructor += d
    if n == constructor:
        const_li.append(i)

if const_li:
    print(min(const_li))
else:
    print(0)