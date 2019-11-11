NK = input().split(' ')
N = int(NK[0])
K = int(NK[1])
An = sorted(list(map(int,input().split(' '))))
Fn = sorted(list(map(int,input().split(' '))),reverse=True)
An_s = sum(An)

min_time = -1 #middle_time = 0を含めるので -1
max_time = An[N-1] * Fn[0] #最大でかかる時間
x_cadidate = An[N-1] * Fn[0] #xの最小の候補
middle_time = -1
range_n = range(N)
#init_list = [0]*N
while True:
    # max_time+1は max_time=0まで求めるため
    middle_time = (min_time + max_time)//2 #二部探索ように 最大と最小の半分を考える この時 middle_time An[i] * Fn[i]の取りうる最大として考える 
    #new_list = init_list
    sum_ax = 0
    for i in range_n:
        ax = middle_time//Fn[i] # An[i] * Fn[i] = x < middle_time より
        if ax < An[i]:
            sum_ax += ax
        else:
            sum_ax += An[i]
    if  min_time+1 == max_time: #二部探索で全てを探索したら終了 
        break
    elif An_s - sum_ax <= K:
        if x_cadidate > middle_time:
            x_cadidate = middle_time 
        max_time = middle_time   #もう少し middle_timeを減らせる
    else:
        min_time = middle_time   #もう少し middle_timeは大きい

print(x_cadidate)