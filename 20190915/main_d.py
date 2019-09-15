import heapq

NM = input().split(' ')
N = int(NM[0])
M = int(NM[1])
AN = input().split(' ')
An = [ int(i)*(-1) for i in AN ] 
heapq.heapify(An)

for _ in range(M):
    max_num = heapq.heappop(An) * (-1)
    cooponed_num = max_num//2
    heapq.heappush(An,cooponed_num*(-1))
print(sum(An) * (-1))