H,W = map(int,input().split(' '))
ans = 0
if H >=2:
    ans += W*(H-1)
if W >=2:
    ans += H*(W-1)
print(ans)