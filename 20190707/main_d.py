N = int(input())
An = list(map(int,input().split(' ')))

a = sum(An[0::2]) - sum(An[1::2])
output_list = [0] * N
output_list[0] = a
last = An[N-1] * 2 - a
output_list[N-1] = last
for i in range(N -2):
    output_list[N-i-2] = An[N-i-2] * 2 - output_list[N-i-1]
print(' '.join(map(str,output_list)))