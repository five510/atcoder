num = int(input())
num_list = input().split(' ')
num_list[0] = int(num_list[0])
for i in range(num):
    num_list[i] = int(num_list[i])
count = 0
for i in range(num):
    if num_list[i] != i+1:
        count = count +1
if count > 2:
    print('NO')
else:
    print('YES')