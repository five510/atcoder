LR = input().split(' ')
L = int(LR[0])
R = int(LR[1])

min_num = 2000000001
flag = False
for l in range(L,R):
    for r in range(l+1,R+1):
        mod = (l*r) %2019
        if mod < min_num:
            min_num = mod
            if mod == 0:
                flag =True
                break
    if flag:
        break

print(min_num)