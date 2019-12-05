N = int(input())
An = list(map(int,input().split(' ')))


cache = [ 0 for _ in range(N+1)] 

cache[0] = 3
amount = 1
mod = 1000000007
for i in range(N):
    need_hat = An[i]
    amount = amount * cache[need_hat] % mod
    cache[need_hat] -= 1
    cache[need_hat+1] += 1
print(amount)
'''
for s_len in range(N+1):
    for c1 in range(3):
        dp[s_len].append([0 for _ in range(N+1)] )
            

dp[0][0][0] = 1
dp[0][1][0] = 1
dp[0][2][0] = 1

for keta in range(1,N+1):
    need_hat = An[keta-1]
    for i in range(3):
        for other_num in range(keta - need_hat - 1):
            for i2 in range(3):
                if i == i2:
                    continue
                other = dp[keta-1][i2][other_num]
                dp[keta][i][need_hat+1] += other
        dp[keta][i][need_hat+1] += dp[keta-1][i][need_hat]
print(dp)
'''
'''
for keta in range(1,N+1):
    need_hat = An[keta-1]
    for i in range(3):
         dp[keta-1][i]
'''