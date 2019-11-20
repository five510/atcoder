N = int(input())
dn = list(map(int,input().split(' ')))
dn.sort()
half_num = N//2
print(dn[half_num]-dn[half_num-1])