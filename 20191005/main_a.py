S = input()
K = int(input())
pre_character = ''
S_list=list(S)
s_len = len(S)
def try_count(pre_character):
    S_list=list(S)
    count = 0
    for i in range(s_len):
        if pre_character == S_list[i]:
            count += 1
            if (s_len - 1) != i:
                S_list[i] = '' #get_abc(pre_character,S_list[i+1])
            else:
                S_list[i] = '' #get_abc(pre_character,S[0])
        pre_character = S_list[i]
    return count,S_list
first_count,fist_list = try_count('')
#print(first_count,fist_list)
second_count,second_list = try_count(fist_list[-1])
#print(second_count,second_list)
third_count,third_list = try_count(second_list[-1])
#print(third_count,third_list)

if second_count == third_count:
    print(first_count+ (second_count*(K-1)))
else:
    gusu = K//2
    kisu = K - gusu
    print((first_count*kisu)+ (second_count*gusu))