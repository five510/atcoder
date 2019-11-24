N = int(input())
An = list(map(int,input().split(' ')))

An_half_sum = sum(An)/2
i = 0
sum_count =0
for i in range(N):
    sum_count += An[i]
    if An_half_sum <= sum_count:
        break
min_num = min(sum_count - An_half_sum, An_half_sum - sum_count + An[i])
print(int(min_num*2))
#print(sum_count - An_half_sum)
#print(An_half_sum - sum_count + An[i])