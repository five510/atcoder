N = int(input())
Dn = list(map(int,input().split(' ')))
#Dn.sort()
previous_num = 0
previous_cnt = 1
current_num = 0
sum_num = 1
flag = False
output_list = [0]* N
max_num = 0
if Dn[0] == 0:
    output_list[0] = 1
    for i in range(1,N):
        max_num = max(max_num,Dn[i]) 
        output_list[Dn[i]] +=1


    '''
    for i in range(1,N):
        if Dn[i] == previous_num + 1:
            current_num += 1
        elif Dn[i] == previous_num + 2:
            if previous_num > 0:
                sum_num = sum_num * (previous_cnt**current_num)
            previous_cnt = current_num
            previous_num += 1
            current_num = 1
        else:
            flag = True
            break
        if i == N-1:
            if previous_num > 0:
                sum_num = sum_num * (previous_cnt**current_num)
    if flag:
        print(0)
    else:
        print(sum_num%998244353)
    '''
    if output_list[0] !=1:
        print(0)
    else:
        for i in range(2,max_num+1):
            sum_num = sum_num * (output_list[i-1]**output_list[i])
        print(sum_num%998244353)
else:
    print(0) 