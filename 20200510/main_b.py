def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

A,B,C,K = read_int_map()
if K <= A:
    print(K)
elif K <= A + B:
    print(A)
else:
    minus = K - (A+B)
    print(A - minus)