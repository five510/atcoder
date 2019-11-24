N,M= map(int,input().split(' '))
KSn =[]
for _ in range(M):
    KS = list(map(int,input().split(' ')))
    K = KS[0]
    Sn = KS[1:K+1]
    KSn.append(Sn)
Pn = list(map(int,input().split(' ')))

def bit_cal2(n):
    return_list = ['']* (2 ** n)
    for i in range(2 ** n):
        for j in range(n):
            if ((i >> j) & 1):
                return_list[i] = return_list[i] + '1'
            else:
                return_list[i] = return_list[i] + '0'
    return return_list

possible_list = bit_cal2(N)
comb_count = 0
for possible in possible_list:
    flag = True
    for i in range(M):
        count = 0
        for i2 in KSn[i]:
            count += int(possible[i2-1])
        if count%2 != Pn[i]:
            flag = False
            break
    if flag:
        comb_count += 1
print(comb_count)    
