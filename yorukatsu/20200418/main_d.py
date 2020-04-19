N,K = map(int,input().split(' '))
an = list(map(int,input().split(' ')))
Sn = [an[0]]
for i in range(1,N):
    Sn.append(Sn[i-1]+an[i])
ans = 0
for i in range(N):
    l = i 
    r = N
    min_border = -1
    while l + 1 <= r:
        m = (l + r)//2
        if i > 0:
            s = Sn[m] - Sn[i - 1]
        else:
            s = Sn[m]
        if s >= K:
            r = m
            min_border = m
        else:
            l = m + 1
    if min_border != -1:
        ans += N - min_border
print(ans)