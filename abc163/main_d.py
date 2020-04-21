N,K = map(int,input().split(' '))
num_list = list(reversed(range(N+1))) 
sum_list_reversed = [num_list[0]]
for i in range(1,N+1):
    sum_list_reversed.append(sum_list_reversed[i-1] + num_list[i])
num_list = list(range(N+1))
sum_list = [num_list[0]]
for i in range(1,N+1):
    sum_list.append(sum_list[i-1] + num_list[i])
ans = 0

for i in range(K-1,N+1):
    current_sum = sum_list_reversed[i] - (sum_list[i] -1)
    ans += current_sum
    ans = ans%(10**9+7)
print(ans)