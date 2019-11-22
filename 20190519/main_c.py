import bisect
import math
N,K = map(int,input().split(' '))
two_list = [ 2**i for i in range(18)]
rate = 0
for i in range(1,N+1):
    threshold = math.ceil(K/i) 
    two_idx = bisect.bisect_left(two_list,threshold)
    rate += 1 / N / two_list[two_idx]
print(rate)