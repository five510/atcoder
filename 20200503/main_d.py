def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

X = read_int()

prime_value  = prime_factorize(X)

def calc(diff,minus=False):
    threads = 10**10
    a = diff
    b = 0
    ## + & +
    while True:
        tmp_x =  (a**5 - b**5)
        if tmp_x == X:
            print(a,b)
            exit(0)
        elif tmp_x > threads:
            break
        elif minus and threads*(-1) > tmp_x:
            break
        a += 1
        b += 1

    a = diff
    b = 0
    ## + & - and -
    while True:
        tmp_x =  (a**5 - b**5)
        if tmp_x == X:
            print(a,b)
            exit(0)
        elif tmp_x > threads:
            break
        elif minus and threads*(-1) > tmp_x:
            break
        a -= 1
        b -= 1
calc(1)
calc(-1,minus=True)
for p in prime_value:
    calc(p)
    calc(p*(-1),minus=True)
    