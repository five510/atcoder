N = int(input())
count_list = [0] * (10**5+1)
count_sum =0
for _ in range(N):
    A = int(input())
    if count_list[A] > 0:
        count_sum += 1
    else:
        count_list[A] +=1
print(count_sum)