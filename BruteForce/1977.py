# 완전제곱수
m = int(input())
n = int(input())

num = 1
squre = []

while True:
    if num * num < m :
        num += 1
    elif num * num >= m and num * num <= n:
        squre.append(num*num)
        num+=1
    elif num * num > n:
        break

if squre:
    print(sum(squre))
    print(min(squre))
else:
    print(-1)
        
