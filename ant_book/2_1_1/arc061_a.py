import copy
S = input()

'''
bit探索
2 進数表記した場合の下から数えて n 桁目（一番下の桁を 0 とします）が 1 であるかどうかをチェックするためのコードは、(i >> n) & 1 
'''
def bit_cal(n):
    return_list = ['']* (2 ** n)
    for i in range(2 ** n):
        for j in range(n):
            if ((i >> j) & 1):
                return_list[i] = return_list[i] + '1'
            else:
                return_list[i] = return_list[i] + '0'
    return return_list

#自作のは遅かった
'''
def bit_cal(max_num,cal_list=[],current_cnt=0):
    new_list = []
    if len(cal_list) == 0:
        for i in range(2):
            new_list.append([i])
    else:
        for cal_val in cal_list:
            for i in range(2):
                tmp = copy.deepcopy(cal_val)
                tmp.append(i)
                new_list.append(tmp)
    current_cnt += 1
    if max_num == current_cnt:
        return new_list
    return bit_cal(max_num,new_list,current_cnt)

'''
all_plus_combination = bit_cal2(len(S)-1)
ans = 0
for plus_combination in all_plus_combination:
    start_idx = 0
    for i in range(len(S)-1):
        if plus_combination[i] == '1':
            ans += int(S[start_idx:i+1])
            start_idx = i+1
    ans +=int(S[start_idx:100])
print(ans)

