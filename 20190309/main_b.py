N,M,C = map(int,input().split(' '))

Bn = list(map(int,input().split(' ')))
Anm =[ list(map(int,input().split(' '))) for _ in range(N)]  

output = 0
for An in Anm:
    sum_amount = C
    for i in range(M):
        sum_amount += An[i]*Bn[i]
    if sum_amount > 0:
        output += 1
print(output)