S = input()

num = len(S)
flag = False
for i in range(num):
    s = S[i]
    if i%2 == 0:
        if s ==  'R' or s ==  'U' or s ==  'D':
            continue
        else:
            flag = True
            break
    else:
        if s ==  'L' or s ==  'U' or s ==  'D':
            continue
        else:
            flag = True
            break

if flag:
    print('No')
else:
    print('Yes')