import itertools
import math

N,D = map(int,input().split(' '))
Xn = [ list(map(int,input().split(' '))) for n in range(N)]
comb_list = list(itertools.combinations(Xn,2))
ans = 0
for comb in comb_list:
    sum_num = 0
    for i,v in enumerate(comb[0]):
        sum_num += (comb[0][i] - comb[1][i])**2
    distance = math.sqrt(sum_num)
    if distance.is_integer():
        ans += 1
print(ans)