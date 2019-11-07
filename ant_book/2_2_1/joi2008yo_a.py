S = 1000 - int(input())
coins = [500,100,50,10,5,1]
used_coins = [0,0,0,0,0,0]
cnt = 0
for i in range(len(coins)):
    while coins[i] == min(S,coins[i]):
        used_coins[i] += 1
        cnt += 1
        S -= coins[i]
print(cnt)
#print(' '.join(map(str,used_coins)))