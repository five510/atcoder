import copy
n,x = map(int,input().split(' '))
Hn = list(map(int,input().split(' ')))
Hn.insert(0,0)
tree_list = [ (Hn[i],[]) for i in range(n+1)]
ans = 0

for i in range(n-1):
    a,b = map(int,input().split(' '))
    tree_list[a][1].append(b)
    tree_list[b][1].append(a)
already_reach = [0]*(n+1)
already_use = [0]*(n+1)
def dfs(a,distance=0,previous_trees=[]):
    global ans
    previous_trees.append(a)
    if already_reach[a] == 1:
        return
    else:
        already_reach[a] = 1
    if tree_list[a][0] == 1:
        ans += distance*2
        distance = 0
        for previous_a in previous_trees:
            already_use[previous_a] = 1
    trees = tree_list[a][1]
    for b in trees:
        if already_use[a] == 1:
            distance = 0
        new_trees = copy.copy(previous_trees) 
        dfs(b,distance+1,new_trees)
dfs(x)
print(ans)