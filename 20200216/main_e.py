N = input()

keta = len(N)

#ans = [0] * ( keta + 1 )
N_list = [0] * (keta+1)
ans_num = 0

for i in reversed(range(keta)):
    N_list[keta-i-1] = int(N[i])

for i in range(keta+1):
    if N_list[i] == 5 and N_list[i+1] >= 5:
        #ans[i] = 0
        N_list[i+1] += 1
        ans_num += 10 - N_list[i]
    elif N_list[i] > 5:
        #ans[i] = 0
        N_list[i+1] += 1
        ans_num += 10 - N_list[i]
    else:
        #ans[i] =  N_list[i]
        ans_num += N_list[i]
#print(ans)
print(ans_num)