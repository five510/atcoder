import sys

sys.setrecursionlimit(4100000)

H,W = map(int,input().split(' '))
area_list = []
for i in range(H):
    area_list.append(list(input()))
#print(area_list)
start_x,start_y = 0,0
goal_idx = [0,0]
for i in range(H):
    for j in range(W):
        if 's' == area_list[i][j]:
            start_x,start_y = i,j
        if 'g' == area_list[i][j]: 
            goal_x,goal_y = i,j
can_move_list = [[0 for _ in range(W)] for _ in range(H)]

def dfs(x,y,target_list,can_move_list): #基本は voidで操作するのが大事 returnさせない
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if x < 0 or H <= x or y < 0 or W <= y: #対象idxがareaの外にいる場合は対象外
        return
    if target_list[x][y] == '#':
        return
    if can_move_list[x][y] == 1: #移動済みの場合は再度dfsをしない
        return
    can_move_list[x][y]= 1 #移動済みの印を付ける
    for i in range(4):
        next_x,next_y = x+dx[i],y+dy[i]
        dfs(next_x,next_y,target_list,can_move_list)

dfs(start_x,start_y,area_list,can_move_list)
if can_move_list[goal_x][goal_y] == 1:
    print('Yes')
else:
    print('No')
