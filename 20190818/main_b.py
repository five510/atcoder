N = int(input())
An = input().split(' ')
sum_num = 0
for i in range(N):
    sum_num +=  1 / int(An[i])
print(1/sum_num)