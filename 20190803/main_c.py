num = int(input())
num_list = input().split(' ')
num_list.reverse()
num_list[0] = int(num_list[0])
for i in range(num):
    if i + 1 == num:
        print('Yes')
        break
    num_list[i+1] = int(num_list[i+1])
    if num_list[i] >= num_list[i+1]:
        continue
    else:
        if num_list[i] + 1 == num_list[i+1]:
            num_list[i+1] = num_list[i+1] -1
        else:
            print('No')
            break