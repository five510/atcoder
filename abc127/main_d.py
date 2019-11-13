import heapq
N,M = map(int,input().split(' '))
An = list(map(int,input().split(' ')))
heapq.heapify(An)
BC_list = []
for i in range(M):
    BC = list(map(int,input().split(' ')))
    BC_list.append(BC)
BC_list.sort(reverse=True,key=lambda x: x[1])
flag = False
decided_sum = []
for val in BC_list:
    B = val[0]
    C = val[1]
    for i in range(B):
        tmp_min = heapq.heappop(An)
        if tmp_min > C:
            #heapq.heappush(An,tmp_min)
            decided_sum.append(tmp_min)
            flag = True
            break
        decided_sum.append(C)
        if len(An) == 0:
            flag = True
            break
    if flag:
        break
print(sum(decided_sum) + sum(An))