N = int(input())
An = input().split(' ')
ball_list = [0] * N
output_list = []
count = 0
for i in range(N):
    sum_amari = sum(ball_list[(N - i -1)::(N - i)])
    if sum_amari % 2 != int(An[N - i -1]): 
        ball_list[N - i -1] = 1
        output_list.append(str(N - i))
output_list.reverse()
print(len(output_list))
if len(output_list) > 0:
    print(' '.join(output_list))
