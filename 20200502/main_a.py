def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]


K = read_int()
A,B = read_int_map()
for i in range(A,B+1):
    if i%K == 0:
        print('OK')
        exit(0)
print('NG')