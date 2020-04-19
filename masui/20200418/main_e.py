N,C = map(int,input().split(' '))
Xn = [ list(map(int,input().split(' '))) for n in range(N)]

pre_xn_sum = [ (Xn[0][1] - Xn[0][0]*2,0) ] # (s,max_idx)
post_xn_sum = []

def get_pre_xn_sum(distance=1):
    pre_xn_sum = [ (Xn[0][1] - Xn[0][0]*distance,0) ] # (s,max_idx)
    for i in range(1,N):
        cuurent_v = pre_xn_sum[i-1][0] + Xn[i][1] - ( Xn[i][0] - Xn[i-1][0] ) *distance
        previous_max_idx = pre_xn_sum[i-1][1]
        if pre_xn_sum[previous_max_idx][0] > cuurent_v:
            max_idx = previous_max_idx
        else:
            max_idx = i
        pre_xn_sum.append((cuurent_v,max_idx))
    return pre_xn_sum

def get_post_xn_sum(distance=1):
    post_xn_sum = [ (Xn[N-1][1] - (C-Xn[N-1][0])*distance,0) ] # (s,max_idx)
    for i in range(1,N):
        xn_i = N - 1 - i
        cuurent_v = post_xn_sum[i-1][0] + Xn[xn_i][1] - ( Xn[xn_i+1][0] - Xn[xn_i][0] ) *distance
        previous_max_idx = post_xn_sum[i-1][1]
        if post_xn_sum[previous_max_idx][0] > cuurent_v:
            max_idx = previous_max_idx
        else:
            max_idx = i
        post_xn_sum.append((cuurent_v,max_idx))
    return post_xn_sum

pre_xn_sum = get_pre_xn_sum(1)
pre_xn_sum_2 = get_pre_xn_sum(2)
post_xn_sum = get_post_xn_sum(1)
post_xn_sum_2 = get_post_xn_sum(2)

ans_1 = 0
ans_2 = 0

# pre_xn_sum && post_xn_sum_2
for i in range(N+1):
    x = i -1
    y = N - 1 - i
    tmp_ans = 0
    if x >= 0:
        x_max_idx = pre_xn_sum[x][1]
        x_max = pre_xn_sum[x_max_idx][0]
        tmp_ans += max(x_max,0)
    if y >= 0:
        y_max_idx = post_xn_sum_2[y][1]
        y_max = post_xn_sum_2[y_max_idx][0]
        tmp_ans += max(y_max,0) 
    ans_1 = max(ans_1,tmp_ans)

# pre_xn_sum && post_xn_sum_2
for i in range(N+1):
    x = i -1
    y = N - 1 - i
    tmp_ans = 0
    if x >= 0:
        x_max_idx = pre_xn_sum_2[x][1]
        x_max = pre_xn_sum_2[x_max_idx][0]
        tmp_ans += max(x_max,0)
    if y >= 0:
        y_max_idx = post_xn_sum[y][1]
        y_max = post_xn_sum[y_max_idx][0]
        tmp_ans += max(y_max,0) 
    ans_1 = max(ans_1,tmp_ans)

print(max(ans_1,ans_2))