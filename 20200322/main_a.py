import math

N,M = map(int,input().split(' '))
count = 0

if N > 1:
    count += N*(N-1)//2
if M > 1:
    count += M*(M-1)//2
print(int(count))