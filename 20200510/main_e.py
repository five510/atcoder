def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

def nCk(n, k):
    ret = 1
    mo = 998244353
    for i in range(k):
        ret = ret * (n - i) * pow(i + 1, mo - 2, mo) % mo
    return ret

N,M,K = read_int_map()
mod = 998244353
base = M * ((M-1)**(N-1)) % mod
mod_sum = base  
for i in range(1,K+1):
    comb = nCk(N-1,i)
    mod_sum += ( base * comb ) % mod
print(mod_sum)
