N,M = map(int,input().split(' '))
ABn = [ list(map(int,input().split(' '))) for _ in range(N)]
ABn.sort()
cnt = 0
ans = 0
for i in range(N):
    if cnt + ABn[i][1] < M:
         cnt += ABn[i][1]
         ans += ABn[i][1] * ABn[i][0]
    else:
        diff = M - cnt
        ans += diff * ABn[i][0]
        break
print(ans)