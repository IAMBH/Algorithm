# 셀프 넘버
# 1~10000 돌면서 각 숫자에 대해 리스트에서 제거

# 1~10000
li = [i for i in range(1,10001)]

for num in range(1, 10001):
    # 각 자리수 더하기
    const = num
    for d in range(len(str(num))):
        const += int(str(num)[d])
    # 리스트에 숫자가 있으면 제거 
    if const in li:
        li.remove(const)
        
# 남은 숫자들 출력    
for num in li:
    print(num)

# 성공