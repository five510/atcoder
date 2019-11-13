N,M = map(int,input().split(' '))

An = [ input() for _ in range(N)]
Bn = [ input() for _ in range(M)]
flag = False
for i in range(N-M+1):
    for j in range(N-M+1):
        for s in range(M):
            a = An[i+s][j:j+M]
            b =Bn[s]
            if An[i+s][j:j+M] != Bn[s]:
                break
            if s == M-1:
                flag = True
print('Yes' if flag else 'No')