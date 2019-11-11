S = input()
s_len = len(S)

s_kigo_map = [] # [[0,1],[1,2]] 0 = < , 1 = >
init_s = S[0]
right_count = 0
left_count = 0
max_len = 0
if S[0] == '<':
    s_num = 0
else:
    s_num = 1
s_count = 1
for i in range(1,s_len):
    if S[0] == '<':
        right_count += 1
    else:
        left_count += 1
    if init_s == S[i]:
        s_count += 1
    else:
        if max_len < s_count:
            max_len = s_count
        s_kigo_map.append([s_num,s_count])
        if S[i] == '<':
            s_num = 0
        else:
            s_num = 1
        init_s = S[i]
        s_count = 1
s_kigo_map.append([s_num,s_count])

next_num = 0
sum_num = 0

i = 0
if len(s_kigo_map) == 1:
    sum_num += (0 +s_kigo_map[i][1] )*(s_kigo_map[i][1]+1)//2
    print(sum_num)
else:
    if s_kigo_map[i][0] == 0: # <の時
        if s_kigo_map[i][1] >= s_kigo_map[i+1][1]:
            sum_num += (0 +s_kigo_map[i][1] )*(s_kigo_map[i][1]+1)//2
            #next_num = next_num + s_kigo_map[i][0]
        else: # `差分を増やす必要がある`
            sum_num += ( (0 +s_kigo_map[i][1] )*(s_kigo_map[i][1]+1)//2 )+ ( s_kigo_map[i+1][1] - s_kigo_map[i][1])
            #next_num = next_num + s_kigo_map[i+1][0] 
    else:  # >の時
        sum_num += (0 +s_kigo_map[i][1] )*(s_kigo_map[i][1]+1)//2
        #next_num = 0

    for i in range(1,len(s_kigo_map)):
        if s_kigo_map[i][0] == 0: # <の時
            if i == len(s_kigo_map) -1:
                sum_num += (1 +s_kigo_map[i][1] )*s_kigo_map[i][1]//2
                break
            if s_kigo_map[i][1] >= s_kigo_map[i+1][1]:
                sum_num += (1 +s_kigo_map[i][1] )*s_kigo_map[i][1]//2
                #next_num = next_num + s_kigo_map[i][0]
            else: # `差分を増やす必要がある`
                sum_num += ( (1 +s_kigo_map[i][1])*s_kigo_map[i][1]//2 ) + ( s_kigo_map[i+1][1] - s_kigo_map[i][1])
                #next_num = next_num + s_kigo_map[i+1][0] 
        else:  # >の時
            sum_num += (s_kigo_map[i][1] - 1 )*(s_kigo_map[i][1])//2
            #next_num = 0
    print(sum_num)