N = int(input())
Ln = list(map(int,input().split(' ')))
max_num = 0
sum_num = 0
for l in Ln:
    sum_num += l
    max_num = max(max_num,l)
if sum_num - max_num > max_num:
    print('Yes')
else:
    print('No')