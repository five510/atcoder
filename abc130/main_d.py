N,K = map(int,input().split(' '))
An = list(map(int,input().split(' ')))

'''
min_border = 0
current_sum = 0
result_count = 0
for i in range(N):
    while current_sum < K and min_border < N:
        current_sum += An[min_border]
        min_border += 1
    if min_border == N and current_sum < K:
        break
    result_count += (N - min_border +1)
    current_sum -= An[i]
print(result_count)
'''


#累積和ように先に計算しておく
Sn = [0] * (N+1)
for i in range(1,N+1):
    Sn[i] = An[i-1] + Sn[i-1]

#二部探索する
result_count = 0
for i in range(N):
    l = i +1
    r = N +1
    min_border = -1
    while l + 1 <= r:
        m = (l + r)//2
        if K <= (Sn[m] - Sn[i]):
            min_border = m
            r = m
        else:
            l = m +1
    if min_border != -1:
        result_count += N - (min_border -1)
print(result_count)

