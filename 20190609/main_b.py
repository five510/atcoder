N = int(input())
Wn = list(map(int,input().split(' ')))

min_indx = -1
min_diff = 10**9
for i in range(1,N):
    before = sum(Wn[0:i])
    after = sum(Wn[i:N])
    min_sum = min(before,after)
    max_sum = max(before,after)
    if (max_sum - min_sum ) < min_diff:
        min_indx = i
        min_diff = max_sum - min_sum
print(min_diff)
