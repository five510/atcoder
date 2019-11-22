import sys
sys.setrecursionlimit(4100000)
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,w = map(int,input().split(' '))
    graph[u].append((v,w))
    graph[v].append((u,w))
color_list = [-1]*(N+1)
color_list[1] = 0
def search(n):
    for node in graph[n]:
        if node[1]%2 ==0:
            num =  color_list[n]
        else:
            num =  0 if color_list[n] == 1 else 1
        if color_list[node[0]] == -1:
            color_list[node[0]] = num
            search(node[0]) 
search(1)
#print(color_list)
for i in range(1,N+1):
    print(color_list[i])