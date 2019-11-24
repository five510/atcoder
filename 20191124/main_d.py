import sys
sys.setrecursionlimit(4100000)
N = int(input())
tree = [[] for _ in range(N+1) ]
already_make = [-1]*(N+1)
for i in range(1,N):
    a,b = map(int,input().split(' '))
    tree[a].append([b,i])

last_color = 0
bfs_use_coler = [[] for _ in range(N+1)]

def solve(n,last_color):
    '''
    use_colers =[]
    for val in bfs_use_coler[0:n-2]:
        use_colers = use_colers + val
    '''
    for val in tree[n]:
        if already_make[val[1]] != -1:
            continue
        use_coloer = -1
        length = last_color+1
        a_tree = list(set(list(range(1,length))) - set(bfs_use_coler[val[0]]) )
        b_tree = list(set(list(range(1,length)))  - set(bfs_use_coler[n])) 
        ab_tree = list(set(a_tree)& set(b_tree))
        '''
        for i in range(1,length):
            if i in bfs_use_coler[val[0]] or i in bfs_use_coler[n]:
                continue
            else:
                use_coloer = i
                break
        if use_coloer == -1:
            last_color +=1
            use_coloer = last_color
        '''
        if len(ab_tree) > 0:
            use_coloer = ab_tree[0]
        else:
            last_color +=1
            use_coloer = last_color
        bfs_use_coler[val[0]].append(use_coloer)
        bfs_use_coler[n].append(use_coloer)
        already_make[val[1]] = use_coloer
    return last_color

for i in range(1,N+1):
    last_color = solve(i,last_color)
print(last_color)
for val in already_make[1:N]:
    print(val)




'''
import sys
sys.setrecursionlimit(4100000)
N = int(input())
tree = [[] for _ in range(N+1) ]
already_make = [-1]*(N+1)
for i in range(1,N):
    a,b = map(int,input().split(' '))
    tree[a].append([b,i])

last_color = 0
bfs_use_coler = [[ -1 for _ in range(N+1) ] for _ in range(N+1) ] 

def solve(n,last_color):
    for val in tree[n]:
        if already_make[val[1]] != -1:
            continue
        use_coloer = -1
        length = last_color+1
        for i in range(1,length):
            if bfs_use_coler[val[0]][i] == 1 or bfs_use_coler[n][i] == 1:
                continue
            else:
                use_coloer = i
                break
        if use_coloer == -1:
            last_color +=1
            use_coloer = last_color
        bfs_use_coler[val[0]][use_coloer] = 1
        bfs_use_coler[n][use_coloer] = 1
        already_make[val[1]] = use_coloer
    return last_color

for i in range(1,N+1):
    last_color = solve(i,last_color)
print(last_color)
for val in already_make[1:N]:
    print(val)
'''