import math
ND = input()
N = int(ND.split(' ')[0])
D = int(ND.split(' ')[1])

num = math.ceil(N / (1+D*2))
print(num)