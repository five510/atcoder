def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]
import math
A,B,N = read_int_map()

if N < B:
    print(math.floor(A*N/B)-A*math.floor(N/B))
else:
    print(math.floor(A*(B-1)/B)-A*math.floor((B-1)/B))

'''
for i in range(1,N+1):
    print(i, math.floor(A*i/B)-A*math.floor(i/B))
'''