import math
abx = input().split(' ')

a = int(abx[0])
b = int(abx[1])
x = int(abx[2])

all_S =a*a*b
empty_area = all_S -x
#print(x,empty_area)
if empty_area > x:
    small_s = (all_S/2) - (empty_area - (all_S/2))
    y = ((small_s*2)/(a*b) -a) *(-1)
    sita = math.degrees(math.atan((a - y)/b))
    print(90 - sita)
else:
    y = ((empty_area*2/(a*a))-b) * (-1)
    #print(y)
    sita = math.degrees(math.atan((b - y)/a))
    print(sita)