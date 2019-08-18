N = int(input())
max_num = (0,0) #(数値,idx)
max_candi = (0,0) #(数値,idx)
for i in range(N):
    A = int(input())
    if max_candi[0] < A and max_num[0] < A:
        max_candi = max_num
        max_num = (A,i)
    elif max_candi[0] < A:
        max_candi = (A,i)

for i in range(N):
    if i == max_num[1]:
        print(max_candi[0])
    else:
        print(max_num[0])