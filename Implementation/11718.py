# 11718 그대로 출력하기
words = []
for i in range(100):
    try:
        a = input()
        words.append(a)
    except EOFError:
        pass

for word in words:
    print(word)

# import sys
# for _ in range(100):
#     print(sys.stdin.readline().strip())