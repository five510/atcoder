A,B,K = map(int,input().split(' '))

if K - A > 0:
    print(0,max(0,(B - (K - A))))
else:
    print(A-K,B)