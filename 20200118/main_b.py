N = int(input())
robots = []
for _ in range(N):
    X,L = map(int,input().split(' '))
    x = X-L
    l = 2*L
    robots.append([x,l+x])
robots.sort()
#print(robots)

cnt = 0
start = robots[0][0]
end = robots[0][1]
result = []
for i in range(1,N):
    x = robots[i][0]
    l = robots[i][1]
    if x < end:
        if end < l:
            continue
        else:
            start = x
            end = l
    else:
        result.append([start,end])
        start = x
        end = l
print(len(result)+1)