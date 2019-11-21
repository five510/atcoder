N,L = map(int,input().split(' '))
sum_apple_pie = 0
min_abs_apple = float('inf')
min_num = float('inf')
for i in range(N):
    sum_apple_pie += i + L
    if abs(i + L) < min_abs_apple:
        min_abs_apple = abs(i + L)
        min_num = i + L
print(sum_apple_pie - min_num)