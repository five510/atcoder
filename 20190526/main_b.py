N = int(input())
SPn =[]
for i in range(N):
    SP = input().split(' ')
    S = SP[0]
    P = int(SP[1])
    SPn.append([S,P,i+1])
SPn.sort()
first_val = SPn[0][0]
current_list = [SPn[0]]
for i in range(1,N):
    if first_val == SPn[i][0]:
        current_list.append(SPn[i])
    else:
        current_list.sort(key=lambda x:(x[1]), reverse=True)
        for val in current_list:
            print(val[2])
        current_list = [SPn[i]]
        first_val = SPn[i][0]
current_list.sort(key=lambda x:(x[1]), reverse=True)
for val in current_list:
    print(val[2])