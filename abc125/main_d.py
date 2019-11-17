N = int(input())
An = list(map(int,input().split(' ')))

sum_list = [ ]
nagative_count = 0
for i in range(N):
    if An[i] < 0 :
        sum_list.append(An[i]*(-1))
        nagative_count += 1
    else: 
        sum_list.append(An[i])

if nagative_count%2 == 0:
    print(sum(sum_list))
else:
    sum_list.sort()
    sum_list[0] = sum_list[0]*(-1)
    print(sum(sum_list))