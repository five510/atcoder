import math
mod = (10**9) + 7

def kaijo(n):
    result = 1
    for i in reversed(range(1,n+1)):
        result = (result * i) % mod
    return result
def combinations_count(n, r):
    return (kaijo(n)) //(kaijo(n - r) * kaijo(r))

def nCk(n, k):
    ret = 1
    mo = 10**9 + 7
    for i in range(k):
        ret = ret * (n - i) * pow(i + 1, mo - 2, mo) % mo
    return ret


X,Y = map(int,input().split(' '))

if (X+Y)%3 == 0:
    flag = False
    if X > Y:
        diff = X - Y
        all_num = (X+Y)//3
        count_2 = Y - all_num
        if X > Y*2:
            flag = True
    elif Y > X:
        diff = Y - X
        all_num = (X+Y)//3
        count_2 = X - all_num
        if Y > X*2:
            flag = True
    else:
        all_num = (X+Y)//3
        count_2 = all_num//2
    if flag:
        print(0)
    else:
        print(nCk(all_num,count_2))
else:
    print(0)
'''
flag = True
x1=0
x2=0
y1=0
y2=0
while flag:
    if X <= Y:
        Y -=2
        y2 += 1
        X -=1
        x1 += 1
    else:
        X -=2
        x2 += 1
        Y -=1
        y1 += 1
    if X <= 0 or Y <= 0:
        flag = False
if X == 0 and Y == 0:
    print(combinations_count(x1+x2,x1))
else:
    print(0)
'''
