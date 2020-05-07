S = input()
ans = 0
for i1 in range(len(S)):
    for i2 in range(i1+1,len(S)+1):
        num = int(S[i1:i2])
        if num%2019 == 0:
            ans += 1

print(ans)