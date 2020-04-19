N = int(input())
An = list(map(int,input().split(' ')))

dp = {}
for a in An:
    if not a in dp:
        dp[a] = 1
    else:
        dp[a] += 1
count = 0
for v in dp.values():
    if v > 1:
        count += v*(v-1)//2
for a in An:
    v = dp[a] 
    diff = 0
    if dp[a] > 1:
        diff = (v*(v-1)//2) - ((v-1)*(v-2)//2)
    print(count-diff)