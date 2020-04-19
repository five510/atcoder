An = []
candidate = []
for i in range(3):
    candidate.append([0,0,0])
    An.append(list(map(int,input().split(' ')))) 
N = int(input())
Bn = []
for i in range(N):
    b = int(input())
    for i1 in range(3):
        for i2 in range(3):
            if b == An[i1][i2]:
                candidate[i1][i2] = 1

for i in range(3):
    if candidate[i][0] == 1 and candidate[i][1] == 1 and candidate[i][2] == 1:
        print('Yes')
        exit(0)  
for i in range(3):
    if candidate[0][i] == 1 and candidate[1][i] == 1 and candidate[2][i] == 1:
        print('Yes')
        exit(0) 

if candidate[0][0] == 1 and candidate[1][1] == 1 and candidate[2][2] == 1:
    print('Yes')
    exit(0) 
elif candidate[0][2] == 1 and candidate[1][1] == 1 and candidate[2][0] == 1:
    print('Yes')
    exit(0)
else:
    print('No')