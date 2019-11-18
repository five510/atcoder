N,K = map(int,input().split(' '))
S = input()
if S[0] == 'L':
    search_s = 'R'
    non_search_s = 'L'
else:
    search_s = 'L'
    non_search_s = 'R'
i = 0
new_S = ''
previous_s = S[0]
while K != 0 and i != N:
    if previous_s != S[i]:
        if previous_s == search_s:
            K -= 1
        previous_s = S[i]        
    i += 1
if K > 0:
    print(N-1)
else:
    new_S += non_search_s*(i-1)
    new_S += S[i-1:N]
    count_s = 0
    previous_s = new_S[0]
    for i in range(1,N):
        if previous_s == new_S[i]:
            count_s +=1
        else:
            previous_s = new_S[i]
    print(count_s)

'''
continue_flag = False
search_list = []
last_S = -5
'''

'''
for i in range(1,N):
    if S[i] == search_s and continue_flag:
        if i + 1 == N:
            last_S = i+1-previous_idx
        continue
    elif S[i] == search_s:
        continue_flag = True
        previous_idx = i
        if i + 1 == N:
            last_S = i+1-previous_idx
    elif continue_flag:
        search_list.append(i-previous_idx)
        continue_flag = False
if last_S == -5:
    last_S = 0
print(search_list)
search_list.sort(reverse=True)
for i in range(K-1):
    if len(search_list) == i:
        break
    search_list[i] = 0
if last_S > 0:
    len_remain_s = len(search_list)+1 - K
else:
    len_remain_s = len(search_list) - K
if len(search_list)+1 <= K:
    last_S = 0
    #len_remain_s -= 1
else:
    if last_S > search_list[K-1]:
        last_S = 0
        #len_remain_s -= 1
    else:
        search_list[K-1] = 0
if len_remain_s <= 0:
    print(N-1)
else:
    if last_S == 0:
        print(search_list)
        print(N -(len_remain_s+1)-sum(search_list))
    else:
        print(N -(len_remain_s)-sum(search_list)-last_S)
'''