N,M = map(int,input().split(' '))
An = list(map(int,input().split(' ')))

if N - sum(An) >=0:
    print(N - sum(An))
else:
    print(-1)
    