a,b = map(int,input().split(' '))

if a > b:
    print(str(b)*a)
elif b > a:
    print(str(a)*b)
elif a == b:
    print(str(a)*b)