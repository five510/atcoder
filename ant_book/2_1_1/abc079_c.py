ABCD = input()

def bit_cal(n):
    return_list = [''] * (2**n)
    for i in range(2**n):
        for j in range(n):
            if ((i >> j) & 1):
                return_list[i] = return_list[i] + '1'
            else:
                return_list[i] = return_list[i] + '0'
    return return_list

ope_candidates = bit_cal(3)

flag = False
for ope in ope_candidates:
    tmp_ans = int(ABCD[0])
    tmp_str = ABCD[0]
    for i in range(3):
        if ope[i] == '0':
            tmp_ans += int(ABCD[i+1])
            tmp_str = tmp_str + '+' + str(ABCD[i+1])
        else:
            tmp_ans -= int(ABCD[i+1])
            tmp_str = tmp_str + '-' + str(ABCD[i+1])
    if tmp_ans == 7:
        break
print(tmp_str + '=7')