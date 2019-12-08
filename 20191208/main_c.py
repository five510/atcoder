import itertools
N = int(input())
An = []
for _ in range(N):
    A = int(input())
    tmp = []
    for _ in range(A):
        tmp.append(list(map(int,input().split(' '))))
    An.append(tmp)

seq = []
for i in range(N):
   seq.append(i) 
max_num = 0
for i in range(N):
    comb_list = list(itertools.combinations(seq,i))
    for comb in comb_list:
        tmp = [-1]*N
        flag = True
        for i2 in range(N):
            if i2 in comb:
                continue
            for xy in An[i2]:
                if tmp[xy[0]-1] == -1:
                    tmp[xy[0]-1] = xy[1]
                else:
                    if tmp[xy[0]-1] != xy[1]:
                        flag = False
        for i2 in range(N):
            if i2 in comb: #`usotuki`
                if tmp[i2] == 1:
                    flag = False
            else:
                if tmp[i2] == 0:
                    flag = False
        if flag:
            max_num = N - i
    if max_num > 0:
        break
print(max_num)