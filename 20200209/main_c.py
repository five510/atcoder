N = int(input())
An = list(map(int,input().split(' ')))
D = {}
for a in An:
    if a in D:
        print('NO')
        exit(0)
    else:
        D[a] = 1
print('YES')

