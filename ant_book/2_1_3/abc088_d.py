import sys

sys.setrecursionlimit(4100000)

H,W = map(int,input().split(' '))
sx,sy = 0,0
move_list = [ list(input()) for _ in range(H) ]
possible_list = [ [-1 for _ in range(W) ] for _ in range(H) ]
possible_list[sx][sy] = 0

x_start_list = [sx]
y_start_list = [sy]

def bfs(target_list,possible_list,x_queue,y_queue,cnt=0):
    x_list = [1,-1,0,0,]
    y_list = [0,0,1,-1]
    cnt += 1
    next_x_queue = []
    next_y_queue = []

    for i in range(4):
        for j in range(len(x_queue)):
            dx = x_queue[j] + x_list[i]
            dy = y_queue[j] + y_list[i]
            if dx < 0 or H <= dx or dy < 0 or W <= dy:
                continue
            if target_list[dx][dy] == '#':
                continue
            if possible_list[dx][dy] != -1:
                continue
            possible_list[dx][dy] = cnt
            next_x_queue.append(dx)
            next_y_queue.append(dy)
    if len(next_x_queue) > 0:
        bfs(target_list,possible_list,next_x_queue,next_y_queue,cnt)
    else:
        return

bfs(move_list,possible_list,x_start_list,y_start_list)

cnt_all_panel = 0
for row in move_list:
    for val in row:
        if val == '.':
            cnt_all_panel += 1
if possible_list[H-1][W-1] == -1:
    print(-1)
else:
    print(cnt_all_panel - possible_list[H-1][W-1] -1)
