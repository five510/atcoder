'''
treelist
[
    [1,2],
    [3],
    [4]
]
'''

NQ = input().split(' ')
N = int(NQ[0])
Q = int(NQ[1])
out_put_list = [0] * N
tree_list = [[] for i in range(N)]

for i in range(N-1):
    ab = input().split(' ')
    a = int(ab[0]) -1
    b = int(ab[1]) -1
    tree_list[a].append(b)

for _ in range(Q):
    px = input().split(' ')
    p = int(px[0])
    x = int(px[1])
    out_put_list[p-1] += x

for i in range(len(tree_list)):
    for num in tree_list[i]:
        out_put_list[num] += out_put_list[i]

print(*out_put_list)