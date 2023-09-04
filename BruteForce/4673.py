# 셀프 넘버
# 1~10000 돌면서 각 숫자에 대해 다시 1부터 돌면서 생성자가 있는지 확인

# 1~10000
li = [i for i in range(1,10001)]

for num in range(1, 10001):
    # 각 자리수 더하기
    const = num
    for d in range(len(str(num))):
        const += int(str(num)[d])
    
    if const in li:
        li.remove(const)
        
for num in li:
    print(num)

# 성공