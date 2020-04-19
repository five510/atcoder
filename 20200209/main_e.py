N = int(input())
K = int(input())

DP = [[0] * 4 ] * 101
for i in range(100):
    if 2 > i:
        DP[i][0] = 1
        DP[i][1] = 10**i - DP[i-1][0]
    else:
