N,M,V,P = map(int,input().split(' '))
An = list(map(int,input().split(' ')))
An.sort(reverse=True)
threadhold_list = [0] * N
theard_num = An[P-1]
theard_idx = 0
sum_An = [0] * N
sum_An[0] = An[0]
for idx,val in enumerate(An):
    if theard_num == val:
        theard_idx = idx
    threadhold_list[idx] = max(0,theard_num-val)
for idx in range(1,N):
    sum_An[idx] = sum_An[idx-1] + An[idx]

#print(An)
#print(threadhold_list)
#print(sum_An)

min_num = 10**10
min_goal_num = 10**10
must_allocation_num = V- (P - 1)
for idx,val in enumerate(An):
    if idx + 1 <= P:
        min_num = min(min_num,val)
        min_goal_num = min(min_goal_num,val)
        continue
    if val == min_num:
        continue
    if threadhold_list[idx] <= M and must_allocation_num <= (N-idx):
        min_num = min(min_num,val)
        continue
    if M < threadhold_list[idx]:
        print(idx)
        exit(0) 
    if (N-idx) < must_allocation_num:
        sum_foword_nums = sum_An[idx-1] - sum_An[(P - 1-1)]
        allocation_diff =  must_allocation_num - (N-idx)
        diveide_allocation_num = (idx-(P - 1))
        plus_sum = (allocation_diff*M)
        last_num = (sum_foword_nums + plus_sum)/diveide_allocation_num
        candidate_num = An[idx] + M
        if last_num <= candidate_num:
            min_num = min(min_num,val)
            continue
    print(idx)
    exit(0)
print(N)

    