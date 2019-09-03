AB = input().split(' ')
A = int(AB[0])
B = int(AB[1])

init_num = 1

count = 0
flag = True

while flag:
    if init_num >= B:
        flag = False
        continue
    init_num += (A -1)
    count += 1
print(count) 
