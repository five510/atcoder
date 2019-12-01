import math
N,M = map(int,input().split(' '))

ABn =[ list(map(int,input().split(' '))) for _ in range(N)]  
ABn.sort(key=lambda x:(x[0]))
amount_yen = 0
for i in range(N):
    if ABn[i][1] < M:
        M -= ABn[i][1]
        amount_yen += ABn[i][0] * ABn[i][1]
    else:
        amount_yen += ABn[i][0] * M
        break
print(amount_yen)
