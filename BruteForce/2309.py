# 일곱 난쟁이
# 전체 돌면서 100이되는 숫자가 되도록 숫자 제외
dwarf_height = [int(input()) for _ in range(9)]

all_height = sum(dwarf_height)
is100 = False

for i in range(8):
    for j in range(i+1, 9):
        if all_height-dwarf_height[i]-dwarf_height[j] == 100:
            dwarf_height.remove(dwarf_height[i])
            dwarf_height.remove(dwarf_height[j])
            is100 = True
            break
            
    if is100 == True:
        break
    
dwarf_height.sort()
for h in dwarf_height:
    print(h)