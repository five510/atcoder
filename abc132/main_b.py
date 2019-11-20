N = int(input())
Pn = list(map(int,input().split(' ')))
count_pn = 0
for i in range(1,N-1):
    if ( Pn[i-1] < Pn[i] < Pn[i+1] ) or ( Pn[i+1] < Pn[i] < Pn[i-1] )        count_pn += 1
print(count_pn)