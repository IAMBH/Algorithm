# 덩치
# 전부 비교해서 자기보다 많은 사람 등수 + 1

n = int(input())
big = [[int(x) for x in input().split()] for i in range(n)]

rank_li = []
rank = 1

for i in range(len(big)):
    for j in range(len(big)):
        if big[i][0]<big[j][0] and big[i][1]<big[j][1]:
            rank += 1
    rank_li.append(rank)
    rank = 1
    
for i in rank_li:
    print(i, end=' ')