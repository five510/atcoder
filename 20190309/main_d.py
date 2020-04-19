import bisect

A,B = map(int,input().split(' '))

bit_list = [1]
for i in range(100000):
    bit_list.append(bit_list[i]*2)
    if bit_list[i+1] > 10**12:
        break

start_point = bisect.bisect_right(bit_list,A)
end_point = bisect.bisect_right(bit_list,B)

start_diff = bit_list[start_point] - A
end_diff = B - bit_list[end_point-1] +1

bit_flag = [0]*end_point



for i in range(1,end_point):
    if end_point - 1 == i:
        if end_diff%2 == 1:
            bit_flag[i] = 1
    wari = end_diff//bit_list[i+1]
    amari = end_diff%bit_list[i+1]
    additional_one = max(0,amari - bit_list[i])
    if additional_one%2  == 1:
        bit_flag[i] = 1

for i in range(1,start_point):
    if not start_diff%bit_list[i+1] >= bit_list[i+1]//2:
        if (start_diff%bit_list[i+1])%2 == 1:
            if bit_flag[i] == 1:
                bit_flag[i] = 0
            else:
                bit_flag[i] = 1

if A%2 == 0:
    if (B-A)%2 == 0:
        bit_flag[0] = ((B-A)//2)%2
    else

print('')