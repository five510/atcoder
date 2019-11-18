N = int(input())
An = list(map(int,input().split(' ')))
Bn = list(map(int,input().split(' ')))
Cn = list(map(int,input().split(' ')))
sum_count = 0
previous_number = -100
for a in An:
    sum_count += Bn[a-1]
    if previous_number + 1 == a:
        sum_count += Cn[previous_number-1]
    previous_number = a
print(sum_count)