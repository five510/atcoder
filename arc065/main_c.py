S = input()

s_i = 0
flag = True
while s_i < len(S) and flag:
    
    if S[s_i:s_i+7] == 'dreamer' and S[s_i:s_i+10]  != 'dreamerase':
        s_i += 7
    elif S[s_i:s_i+5] == 'dream':
        s_i += 5
    elif S[s_i:s_i+6] == 'eraser':
        s_i += 6
    elif S[s_i:s_i+5] == 'erase':
        s_i += 5
    else:
        flag = False
if flag:
    print('YES')
else:
    print('NO')