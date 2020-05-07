def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))
import math

A,B,C,D = read_int_map()
if math.ceil(C/B) > math.ceil(A/D):
    print('No')
else:
    print('Yes')