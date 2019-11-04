NY = input().split(' ')
N = int(NY[0])
Y = int(NY[1])

sum_Y = 0
ans = (-1,-1,-1)
for x in range(N+1):
    for y in range(N+1-x):
        sum_Y = 10000*x + 5000*y + 1000*(N-x-y)
        if sum_Y == Y:
            ans = (x,y,N-x-y)
    
    if x == N:
        sum_Y = 10000*x
        if sum_Y == Y:
            ans = (x,y,N-x-y)
print(' '.join(map(str,ans)))
