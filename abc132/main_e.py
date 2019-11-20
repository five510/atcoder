import sys
sys.setrecursionlimit(4100000)
N,M = map(int,input().split(' '))
already_reach = [-1]*(N+1)
already_reach_1st = [-1]*(N+1)
already_reach_2nd = [-1]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split(' '))
    graph[u].append(v)
S,T = map(int,input().split(' '))
next_list = []
def search_bfs(S_list,current_count=0):
    next_list = []
    for s in S_list:
        for i1 in graph[s]:
            #print(already_reach_1st)
            if already_reach_1st[i1] != -1:
                continue
            already_reach_1st[i1] = 0
            for i2 in graph[i1]:
                #print(already_reach_2nd)
                if already_reach_2nd[i2] != -1:
                    continue
                already_reach_2nd[i2] = 0
                for i3 in graph[i2]:
                    if already_reach[i3] == -1: #はじめての到達
                        already_reach[i3] = current_count+1
                        next_list.append(i3)
    if len(next_list) > 0:
        search_bfs(next_list,current_count+1)
search_bfs([S])
print(already_reach[T])