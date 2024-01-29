# 1120 문자열
a, b = input().split()
cnt = 0
cnt_li = []

for i in range(len(b)-len(a)+1):
    for j in range(len(a)): 
        if a[j] != b[i+j]:
            cnt+=1
    cnt_li.append(cnt)
    cnt=0

print(min(cnt_li))
