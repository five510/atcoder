N = int(input())
An = [ int(input()) for _ in range(N)]

current_partition_cnt = 0
ans = 0
for a in An:
    if a == 0:
        ans += current_partition_cnt//2
        current_partition_cnt = 0
    else:
        current_partition_cnt += a
ans += current_partition_cnt//2
print(ans)