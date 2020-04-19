N,M = map(int,input().split(' '))
SCn = []
candidate = [0]*N
for i in range(M):
    S,C = map(int,input().split(' '))
    if S == 1 and C == 0:
        print(-1)
        exit(0)
    if candidate[S-1] != 0 and candidate[S-1] != C:
        print(-1)
        exit(0)
    else:
        candidate[S-1] = C
    
if candidate[0] == 0:
    candidate[0] = 1
print(''.join(map(str,candidate)))