H,W = map(int,input().split(' '))

An = []
Bn = []
for _ in range(H):
    An.append(list(map(int,input().split(' '))))

for _ in range(H):
    Bn.append(list(map(int,input().split(' '))))

diff_list = []
for h in range(H):
    diff_list.append([])
    for w in range(W):
        diff = max(An[h][w],Bn[h][w]) - min(An[h][w],Bn[h][w]) 
        diff_list[h].append(diff)
print(diff_list)