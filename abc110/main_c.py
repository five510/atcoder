S = input()
T = input()

replace_to =[]
flag = False
for i in range(len(S)):
    if S[i] != T[i]:
        if S[i] in replace_to or T[i] in replace_to:
            flag = True
            break
        else:
            S = S.replace(T[i], '0').replace(S[i], T[i]).replace('0', S[i])
            replace_to.append(S[i])

if flag:
    print('No')
else:
    print('Yes')