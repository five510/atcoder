N,K,S = map(int,input().split(' '))

result = []
for i in range(N):
    if i < K:
        result.append(S)
    else:
        if S == 10**9:
            result.append(S-1)
        else: 
            result.append(S+1)
print(' '.join(map(str,result)))