N = int(input())
flag = False
for i in range(1,10):
    for s in range(1,10):
        if i*s == N:
            flag = True
if flag:
    print('Yes')
else:
    print('No')