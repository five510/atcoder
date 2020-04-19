import heapq

N,K = map(int,input().split(' '))
pn = list(map(int,input().split(' ')))
#Sn = [0] * N
#Sn[0] = pn[0]
#for i in range(1,len(pn)):
#    Sn[i] = Sn[i-1] + pn[i]
kakuritsu = [0] * N 
num_list = [0] * 1001
num_list[0] = 0
for i in range(1,1001):
    num_list[i] = num_list[i-1] + i

for i in range(N):
    if i != 0:
        kakuritsu[i] = kakuritsu[i-1] + ( num_list[pn[i]] / pn[i] )
    else:
        kakuritsu[i] = num_list[pn[i]] / pn[i]

max_sn = [0] * N

for i in range(N-K+1):
    if i != 0:
        max_sn[i] = ( kakuritsu[i-1+K] - kakuritsu[i-1]   ) * (-1)
    else:
        max_sn[i] = kakuritsu[i-1+K] * (-1)

heapq.heapify(max_sn)
print(heapq.heappop(max_sn) * (-1))