NKQ = input().split(' ')
N = int(NKQ[0])
K = int(NKQ[1])
Q = int(NKQ[2])

Bn = [0] * N
for _ in range(Q):
    A = int(input()) 
    Bn[A-1] += 1

for i in range(N):
    if K - Q + Bn[i]  > 0:
        print('Yes')
    else:
        print('No')