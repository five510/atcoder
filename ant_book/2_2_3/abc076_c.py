S = input()
T = input()
t_len = len(T)
s_len = len(S)
output_list = [''] * len(S)
flag = False
hatena_to_a_str = ''
for i in range(s_len):
    if S[i] == '?':
        hatena_to_a_str += 'a'
    else:
        hatena_to_a_str += S[i]
#print(hatena_to_a_str)
current_min = 'z' * (s_len+1)
for i in reversed(range(s_len-t_len+1)):
    #print(i)
    text = S[i:i+t_len]
    if S[i:t_len] == T:
        flag = False
    else:
        for j in range(t_len):
            if text[j] != T[j] and text[j] != '?':
                break 
            if j == t_len-1:
                flag = True
                for s in range(t_len):
                    output_list[i+s] = T[s]
    if flag:
        tmp = hatena_to_a_str[:i] + T + hatena_to_a_str[i+t_len:s_len]
        current_min = min(current_min,tmp)
        flag = False

if current_min == 'z' * (s_len+1):
    print('UNRESTORABLE')
else:
    print(current_min)