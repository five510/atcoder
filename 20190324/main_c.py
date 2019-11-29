N,Q = map(int,input().split(' '))
S = input()

count_sum_list = [0]*(N+1)
start_A_pointa = [0]*(N+1)

for i in range(1,N+1):
    if i != N and S[i-1] == 'A' and S[i] == 'C':
        count_sum_list[i] = count_sum_list[i-1] + 1
        start_A_pointa[i] = 1
    else:
        count_sum_list[i] = count_sum_list[i-1]
#print(count_sum_list)

output_list = []

for _ in range(Q):
    l,r = map(int,input().split(' '))
    if start_A_pointa[r] == 1:
        output_list.append(count_sum_list[r]-count_sum_list[l-1] -1)
    else:
        output_list.append(count_sum_list[r]-count_sum_list[l-1])

for out in output_list:
    print(out)
