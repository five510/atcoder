N,M = map(int,input().split(' '))
tree_list = [[] for _ in range(N) ]
for _ in range(M):
    L,R,C = map(int,input().split(' '))
    tree_list[R-1].append([C,L-1])
inf = float('inf')
dp = [inf] * N
dp[N-1] = 0
current_num = -1
flag = False
if len(tree_list[N-1]) > 0: 
    for i in reversed(range(N)):
        if dp[i] == inf:
            flag = True
            break
        current_start_paths = tree_list[i]
        if len(current_start_paths) > 0:
            current_start_paths.sort()
            for path in current_start_paths:
                if dp[path[1]] > dp[i] + path[0]:
                    for j in range(path[1],i):
                        if (dp[i] + path[0]) < dp[j]:
                            dp[j] = dp[i] + path[0]
                        else:
                            break
    if dp[0] == inf or flag:
        print(-1)
    else:
        print(dp[0])
else:
    print(-1)


'''
N,M = map(int,input().split(' '))

tree_list = [[] for _ in range(N) ]
LRC = sorted([list(map(int, input().split())) for i in range(M)], key=lambda x: (x[0], x[1]))
inf = float('inf')
dp = [inf] * N
dp[0] = 0
flag = False
if LRC[0][0] != 1:
    print(-1) 
else:
    for l, r, c in LRC:
        l = l -1
        r = r -1
        if dp[r] > dp[l] + c:
            for i in reversed(range(l+1,r+1)):
                if dp[i] > dp[l] + c:
                    dp[i] = dp[l] + c
                else:
                    break 
    if dp[N-1] < inf:
        print(dp[N-1])
    else:
        print(-1)
'''

'''
for _ in range(M):
    L,R,C = map(int,input().split(' '))
    tree_list[R-1].append([C,L-1])
dp = [1000000000000] * N
dp[N-1] = 0
current_num = -1
flag = False
if len(tree_list[N-1]) > 0: 
    for i in reversed(range(N)):
        if dp[i] == 1000000000000:
            flag = True
            break
        current_start_paths = tree_list[i]
        if len(current_start_paths) > 0:
            current_start_paths.sort()
            for path in current_start_paths:
                if dp[path[1]] > dp[i] + path[0]:
                    for j in range(path[1],i):
                        if (dp[i] + path[0]) < dp[j]:
                            dp[j] = dp[i] + path[0]
                        else:
                            break
    if dp[0] == 1000000000000 or flag:
        print(-1)
    else:
        print(dp[0])
else:
    print(-1)
'''