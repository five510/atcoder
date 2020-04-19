N,M,K = map(int,input().split(' '))
friends = [ set() for i in range(N) ]
blocks = [ set() for i in range(N) ]
for i in range(M):
    A,B = map(int,input().split(' '))
    min_n = min(A,B) - 1
    max_n = max(A,B) - 1
    friends[min_n].add(max_n)
    friends[max_n].add(min_n)
for i in range(K):
    A,B = map(int,input().split(' '))
    min_n = min(A,B) - 1
    max_n = max(A,B) - 1
    blocks[min_n].add(max_n)
    blocks[max_n].add(min_n)

#friends_sn = [friends[0]]
#for i in range(1,N):
#    friends_sn[i] = friends_sn[i-1] + friends[i]
friends_chain = [0]*N
if 1 in friends[0]:
    friends_chain[0] = 1
for i in range(1,N):
    if i + 1 in friends[i]:
        friends_chain[i] = friends_chain[i-1] + 1
    else:
        friends_chain[i] = friends_chain[i-1]
all_set = set(range(N))
for i in range(N):
    union_set = friends[i] | blocks[i]
    diff_set = all_set - union_set
    diff_set.sort()
    for target_num in diff_set:
        min_n = min(i,target_num)
        max_n = max(i,target_num)
         
    ans.append(N - 1 - len(cand))
print(' '.join(map(str,ans)))
