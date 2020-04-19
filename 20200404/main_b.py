N,M = map(int,input().split(' '))
An = list(map(int,input().split(' ')))
An.sort(reverse=True)
sum_num = sum(An)
for i in range(M):
    if An[i] < sum_num/(4*M):
        print('No')
        exit(0)
print('Yes')
        