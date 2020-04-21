import math
txa,tya,txb,tyb,T,V = map(int,input().split(' '))
N = int(input())
XYn = [list(map(int,input().split(' '))) for _ in range(N)]

for xy in XYn:
    x = xy[0]
    y = xy[1]
    way1 = math.sqrt((txa-x)**2 + (tya-y)**2)
    way2 = math.sqrt((txb-x)**2 + (tyb-y)**2)
    if (way1+way2) <= (T*V):
        print('YES')
        exit(0)
print('NO')