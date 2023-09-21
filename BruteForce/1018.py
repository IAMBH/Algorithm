# 체스판 다시 칠하기
# 전체를 8x8로 나눴을 때 
n, m = map(int, input().split())
chessboard = []

for _ in range(n):
    row = input()  # 공백 제거하여 입력 받음
    chessboard.append(row)

# WB, BW 따로 가져가기
result_li = []

WB_max = []
BW_max = []

count_WB = 0
count_BW = 0 
count_WB_li = []
count_BW_li = []

# 8x8 중에 wb, bw 둘 중 가장 많은 곳 찾기
for i in range(n-7): # 어디까지 돌지 (몇번돌지)
    for k in range(m-7): # 가로로 하나씩
        for j in range(i, i+8): # 시작줄부터 8줄
            result_li.append(chessboard[j][k:k+8])
        for y in range(0,8):
            for x in range(0, 8):
                # 첫줄이 WBWBWBWBWB 인 경우
                if y%2==0: # 짝수줄
                    if x%2==0: # 짝수번째
                        if result_li[y][x] != 'W':
                            count_WB += 1
                    else:
                        if result_li[y][x] != 'B':
                            count_WB += 1
                else: # 홀수줄
                    if x%2==0: # 짝수번째
                        if result_li[y][x] != 'B':
                            count_WB += 1
                    else:
                        if result_li[y][x] != 'W':
                            count_WB += 1
                            
                # 첫줄이 BWBWBWBWBW 인 경우
                if y%2==0:
                    if x%2==0:
                        if result_li[y][x] != 'B':
                            count_BW += 1
                    else:
                        if result_li[y][x] != 'W':
                            count_BW += 1
                else:
                    if x%2==0:
                        if result_li[y][x] != 'W':
                            count_BW += 1
                    else:
                        if result_li[y][x] != 'B':
                            count_BW += 1
                        
        count_WB_li.append(count_WB)
        count_BW_li.append(count_BW)
        count_WB=0
        count_BW=0
        # print(result_li)
        # print('WB', count_WB_li, 'BW', count_BW_li)
        result_li=[]
        
print(min(min(count_BW_li), min(count_WB_li)))
