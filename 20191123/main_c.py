H,W,K= map(int,input().split(' '))

HW = [ input() for _ in range(H) ]
already_reach = [ [0]*W for _ in range(H) ]

def search(h,w,num):
    hn = [0,1]
    wn = [1,0]
    from_num = 0
    to_num = 0
    w_to = 0
    for i in range(1,W):
        if 0 <= w-i and HW[h+0][w-i] == '.' and already_reach[h+0][w-i] == 0:
            from_num -= 1
        else:
            break
    for i in range(1,W):
        if w+i < W and HW[h+0][w+i] == '.' and already_reach[h+0][w+i] == 0:
            to_num += 1
        else:
            break
    for i in range(from_num,to_num+1):
        already_reach[h][w+i] = num
    
    for s in range(1,H):
        if h + s >= H:
            break
        flag = False
        for i in range(from_num,to_num+1):
            if HW[h+s][w+i] != '.' or already_reach[h+s][w+i] != 0:
                flag = True
                break
        if flag:
            break
        for i in range(from_num,to_num+1):
             already_reach[h+s][w+i] = num
    for s in range(1,H):
        if h - s < 0:
            break
        flag = False
        for i in range(from_num,to_num+1):
            if HW[h-s][w+i] != '.' or already_reach[h-s][w+i] != 0:
                flag = True
                break
        if flag:
            break
        for i in range(from_num,to_num+1):
             already_reach[h-s][w+i] = num
current_num = 1
for s in range(H):
    for i in range(W):
        if HW[s][i] == '#':
            search(s,i,current_num)
            current_num +=1
for s in range(H):
    print(' '.join(map(str,already_reach[s])))