import heapq
NM = input()
N = int(NM.split(' ')[0])
M = int(NM.split(' ')[1])
each_days_list = [[] for _ in range(M)]
 
for i in range(N):
    ab = input()
    a = int(ab.split(' ')[0])
    b = int(ab.split(' ')[1])
    if a <= M:
        each_days_list[a-1].append(b)

max_list = []
salary_count = 0
for i in range(M):
    for j in range(len(each_days_list[i])): 
        heapq.heappush(max_list,-each_days_list[i][j])
    if len(max_list) > 0:
        salary_count += -heapq.heappop(max_list)
        
print(salary_count)