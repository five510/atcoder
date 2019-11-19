import itertools
import math

N = int(input())
XY = [list(map(int,input().split(' '))) for _ in range(N)]
All_combination = list(itertools.permutations(XY))
All_distances = []
for each_list in All_combination:
    distance = 0
    for i in range(1,N):
        distance += math.sqrt((each_list[i-1][0] - each_list[i][0])**2 + (each_list[i-1][1] - each_list[i][1])**2) 
    All_distances.append(distance)
print(sum(All_distances)/len(All_distances))

'''
list_store = [[] * math.factorial(N)]

tmp = range(n)
def fanc(n_list):
    for val in n_list:
        Xn[i]
'''