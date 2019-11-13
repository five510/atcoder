import math
N = int(input())

ans = -1
for i in reversed(range(int(math.sqrt(N)+1))):
    if N % i == 0:
        ans = i
        break
print(len(str(N//ans)))