# 블랙잭
# 다 더해서 리스트에 넣고 max 출력
n, m =  map(int, input().split())
num_li = list(map(int, input().split()))
max_li = []

# 숫자 2개 고정
for x in range(len(num_li)-2):
    for y in range(x+1,len(num_li)):
        for z in range(y+1, len(num_li)):
            s = num_li[x] + num_li[y] + num_li[z]
            if s<=m:
                max_li.append(s)

print(max(max_li))
            