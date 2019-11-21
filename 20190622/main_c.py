A,B,C,D = map(int,input().split(' '))
#最大公約数
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
#最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)
c_num = (B//C - (A-1)//C)
d_num = (B//D - (A-1)//D)
cd_num = (B//lcm(C, D) - (A-1)//lcm(C, D))
print((B-A+1) - (c_num+d_num-cd_num))