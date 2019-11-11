N = int(input())
Bn =  list(map(int,input().split(' ')))

output_list = []

for i in reversed(range(N)):
    current_sum = 0
    target_num = i+1
    target_num_idx = 0
    for j in range((N)//(target_num)):
        target_num_idx = target_num_idx + target_num
        current_sum += Bn[target_num_idx -1]
    if current_sum % 2 != Bn[i]:
        if Bn[i] == 1:
            Bn[i] = 0
        else:
            Bn[i] = 1
    if Bn[i] == 1:
        output_list.append(target_num)
print(len(output_list))
output_list.reverse()
print(' '.join(map(str,output_list)))