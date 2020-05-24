def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

S = input()
T = input()
if S == T[:len(T)-1]:
    print('Yes')
else:
    print('No')