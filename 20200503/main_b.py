def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

N,K = read_int_map()
human = [1]*N
for i in range(K):
    d = read_int()
    An = read_int_list()
    for a in An:
        human[a-1] = 0
print(sum(human))