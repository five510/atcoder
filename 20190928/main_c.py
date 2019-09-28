import heapq
N = int(input())
idx_list = [0] * N
Hn = list(map(int,input().split(' ')))
for i in range(N):
    number = Hn[i]
    idx_list[number -1] = i +1
print(' '.join(map(str,idx_list)))