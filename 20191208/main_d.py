import bisect
N = int(input())
An = list(map(int,input().split(' '))) 

bit_list = [1]
for i in range(100000):
    bit_list.append(bit_list[i]*2)
    if bit_list[i+1] > 2**60:
        break
start_point = bisect.bisect_right(bit_list,max(An))
keta_list = [0] *  start_point

for A in An:
    abin = format(A, 'b')
    for i in range(len(abin)):
        if abin[i] == '1':
            keta_list[len(abin)-1-i] += 1
count = 0
for idx,keta_count in enumerate(keta_list):
    count += (N-keta_count) * bit_list[idx] * keta_count
    count = count % (1000000000+7)
print(count)