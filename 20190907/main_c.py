N = int(input())
Bn = list(map(int,input().split(' ')))
An = [-1 for _ in range(N)]
An[0] = Bn[0]
for i in range(1,N-1):
    An[i] = min(Bn[i-1],Bn[i])
An[N-1] = Bn[N-2]
print(sum(An))