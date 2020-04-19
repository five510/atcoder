N,A,B = map(int,input().split(' '))

if (B - A)%2 == 0:
    print((B - A)//2)
else:
    if A-1 < N-B:
        reach_min = A
        b_num = B - A
        num_second = (b_num-1)//2
        print(reach_min+num_second)
    else:
        reach_min = N - B + 1
        b_num = A + reach_min
        num_second = (N-b_num)//2
        print(reach_min+num_second)