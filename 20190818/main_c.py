import heapq

N = int(input())
Vn = list(map(int,input().split(' ')))
heapq.heapify(Vn)
init_val = heapq.heappop(Vn) 

for _ in range(N -1):
    init_val = (init_val + heapq.heappop(Vn))/2
print(init_val)