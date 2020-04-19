N = int(input())

dp = [0] * 19

if N%2 == 1:
    print(0)
else:
    for i in range(18):
        if i == 0:
            dp[i] = 1
        elif i == 1:
            dp[i] = 10
        else:
            tmp = dp[0:i]
            dp[i] = sum(dp[0:i])*9 + 1
print(dp)
print(sum(dp))