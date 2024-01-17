# 영화감독 숌
# 1부터 무한루프 돌면서 666 들어가는 숫자 세기
n = int(input())
num = 1
count = 0

while(True):
    find_666 = [ int(str(num)[i]) for i in range(len(str(num))) ]
    index_of_6 = list(filter(lambda x : find_666[x] == 6, range(len(find_666))))    # 6의 인덱스
    if len(index_of_6)<3:
        pass
    else:
        ### 6이 연속으로 3개가 있는지 판별
        isContinue = [] # 연속된 인덱스인지
        # 옆에 숫자가 자기자신 +1 이면 True
        for i in range(len(index_of_6)-1):
            if index_of_6[i]+1==index_of_6[i+1]:
                isContinue.append(True)
            else:
                isContinue.append(False)
        # 연속된 3개의 True가 있는가
        for i in range(len(isContinue)-2):
            if isContinue[i]==True and isContinue[i+1]==True and isContinue[i+2]==True:
                count+=1
                break
        ###

    if count == n:
        print(num)
        break 
    num+=1