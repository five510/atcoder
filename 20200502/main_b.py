def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]
import math

X = read_int()
ans = 0
money = 100
while True:
    ans += 1
    money = math.floor(money * 1.01)
    if money >= X:
        print(ans)
        exit(0)