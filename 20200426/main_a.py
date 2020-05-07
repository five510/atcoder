def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

S,W = read_int_map()

if S <= W:
    print('unsafe')
else:
    print('safe')