N = int(input())
dp = [ [] for _ in range(N+1)] 
mod = 10**9 +7

for s_len in range(N+1):
    for c1 in range(4):
        dp[s_len].append([])
        for c2 in range(4):
            dp[s_len][c1].append([0,0,0,0])
dp[0][3][3][3] = 1            

for s_len in range(N):
    for c4 in range(4):
        for c3 in range(4):
            for c2 in range(4):
                if dp[s_len][c2][c3][c4] == 0:
                    continue
                for c1 in range(4):
                    if c3 == 0 and c2 == 1 and c1 == 2:
                        continue
                    if c3 == 1 and c2 == 0 and c1 == 2:
                        continue
                    if c3 == 0 and c2 == 2 and c1 == 1:
                        continue
                    if c4 == 0 and c2 == 1 and c1 == 2:
                        continue
                    if c4 == 0 and c3 == 1 and c1 == 2:
                        continue
                    dp[s_len+1][c1][c2][c3] += dp[s_len][c2][c3][c4]
                    current_num = dp[s_len][c2][c3][c4]
                    dp[s_len+1][c1][c2][c3] = dp[s_len+1][c1][c2][c3]%mod

ans = 0

for c1 in range(4):
    for c2 in range(4):
        for c3 in range(4):
            ans += dp[N][c1][c2][c3]
            ans = ans%mod
print(ans)

