N = int(input())
K = int(input())
ans = 1
for i in range(N):
    if ans > K:
        ans += K
    else:
        ans = ans*2
print(ans)