import sys

sys.setrecursionlimit(4100000)

H,W = map(int,input().split(' '))
sx,sy = map(int,input().split(' '))
gx,gy = map(int,input().split(' '))
move_list = [list(input()) for _ in range(H)]
possible_list = [[-1 for _ in range(W) ] for _ in range(H)]

queue = []
def bfs(target_list,x_queue,y_queue,cnt=0):
    x_list = [1,-1,0,0,]
    y_list = [0,0,1,-1]

    #マスの確定
    '''
    for i in range(len(x_queue)):
        possible_list[x_queue[i]][y_queue[i]] = cnt
    '''
    cnt += 1
    next_x_queue = []
    next_y_queue = []
    #マスの探索
    for i in range(4):
        for j in range(len(x_queue)):
            dx = x_queue[j] + x_list[i]
            dy = y_queue[j] + y_list[i]
            if dx < 0 or H <= dx or dy < 0 or W <= dy: #area外
                continue
            if target_list[dx][dy] == '#': #塀で通れない
                continue
            if possible_list[dx][dy] != -1: #すでに他の組み合わせで探索済み
                continue
            possible_list[dx][dy] = cnt
            next_x_queue.append(dx)
            next_y_queue.append(dy)
    if len(next_x_queue) > 0:
        bfs(target_list,next_x_queue,next_y_queue,cnt)
    else:
        return
start_x_queue = [sx-1]
start_y_queue = [sy-1]
possible_list[sx-1][sy-1] = 0
bfs(move_list,start_x_queue,start_y_queue)
#print(possible_list)
print(possible_list[gx-1][gy-1])