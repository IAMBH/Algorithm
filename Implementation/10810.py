# 10810 공 넣기
n, m = map(int, input().split())
methods = []
for i in range(m):
    methods.append(list(map(int, input().split())))

baguni = [ 0 for i in range(n) ]
for method in methods:
    for i in range(method[0]-1, method[1]):
        baguni[i] = method[2]

print(*baguni)