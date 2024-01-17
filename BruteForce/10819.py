# 차이를 최대로
# 모든 경우의 수
import itertools

n = int(input())
nums = list(map(int, input().split()))

cases = itertools.permutations(nums, n)

sum = []

for case in list(cases):
    s = 0
    for i in range(len(case)-1):
        s += abs(case[i] - case[i+1])
    sum.append(s)

print(max(sum))