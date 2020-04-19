N = int(input())
dp = {}
max_num = 0
max_list =[]
for i in range(N):
    S = input()
    if S in dp:
        dp[S] += 1
    else:
        dp[S] = 1
    if dp[S] == max_num:
        max_list.append(S)
    elif dp[S] > max_num:
        max_list = [S]
        max_num = dp[S]
max_list.sort()
for s in max_list:
    print(s)