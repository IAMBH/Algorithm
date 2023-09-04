# 한수 : 각 자리가 등차수열
# 입력 받은 수 보다 작은 수들이 등차인지 싹다 검증
# 등차 검증 : 각 자리 수 뽑아서 리스트에 저장, 뒤에 공간에 저장된 수와의 차가 같은지

num = int(input())
cnt = 0

for i in range(1, num+1):
    # 각 자리수 리스트에 저장
    temp = [ int(str(i)[n]) for n in range(len(str(i))) ]
    # 뒷자리 숫자와의 차를 리스트에 저장, set으로 중복제거하여 0 (일의 자리수) or 1 (십의 자리수 또는 등차수열) 개수 증가
    arithmetic = set([ temp[n]-temp[n+1] for n in range(len(temp)-1)])
    if len(arithmetic)==0 or len(arithmetic)==1:
        cnt+=1

print(cnt)