H,W = map(int,input().split(' '))
move_list = [ list(input()) for _ in range(H) ]
possible_list = [[10**9]*W  for _ in range(H)]

def dfs(x,y,score,is_sequence):
    if x < 0 or H <= x or y < 0 or W <= y: #対象idxがareaの外にいる場合は対象外
        return
    if is_sequence == False and move_list[x][y] == '#':
        score +=1
        is_sequence = True
    elif move_list[x][y] == '.':
        is_sequence = False
    if possible_list[x][y] <= score:
        return
    possible_list[x][y] = score
    dfs(x+1,y,score,is_sequence)
    dfs(x,y+1,score,is_sequence)
dfs(0,0,0,False)
#print(possible_list)
print(possible_list[H-1][W-1])
