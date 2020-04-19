K = int(input())
dp = [['1','2','3','4','5','6','7','8','9'],[]]

cnt = 9
keta = 0
dp_num = 0
while True:
    num = 2
    current_base_num_str = dp[keta][dp_num][-1]
    current_base_num_int = int(current_base_num_str)
    break_flag = False
    for i in range(-1,num):
        if current_base_num_int + i > 9 or current_base_num_int + i < 0:
            continue
        dp[keta+1].append(dp[keta][dp_num] + str(current_base_num_int + i))
        cnt += 1
        if cnt >= K:
            break_flag = True
            break
    if break_flag:
        break
    if dp_num < len(dp[keta])-1:
        dp_num += 1
    else:
        dp_num = 0
        keta += 1
        dp.append([])
if K < 10:
    print(K)
else:
    if len(dp[keta+1]) == 0:
        print(dp[keta][-1])
    else:
        print(dp[keta+1][-1])