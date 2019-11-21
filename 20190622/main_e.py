N,K = map(int,input().split(' '))
max_num = (N-2)*(N-2+1)/2
M = 0
if max_num >=K:
    base_graph = [[] for _ in range(N+1)]
    base_graph[1].append(2)
    base_graph[2].append(1)
    for i in range(3,N+1):
        base_graph[1].append(i)
        base_graph[i].append(1)
    M = N- 1
    idx = N
    diff = max_num-K
    while diff != 0:
        if len(base_graph[idx]) == N-1:
            idx -= 1
        else:
            insert_val = len(base_graph[idx]) + 1 - (N-idx)
            base_graph[idx].append(insert_val)
            base_graph[insert_val].append(idx)
            diff -=1
            M +=1
    print(M)
    for idx,node in enumerate(base_graph): 
        for i in node:
            if idx < i:
                print(idx,i)
else:
    print(-1)
