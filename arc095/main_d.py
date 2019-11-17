import bisect
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input())
An = list(map(int,input().split(' ')))


An.sort()
max_num = An[N-1]

half_val = max_num//2
idx =  bisect.bisect_right(An[0:N-1],half_val)
if idx == 0:
    print(max_num,An[idx])
elif idx == N-1:
    print(max_num,An[idx-1])
else:
    A = An[idx] - half_val
    B = half_val - An[idx-1]
    if A > B:
        print(max_num,An[idx-1])
    else:
        print(max_num,An[idx])

