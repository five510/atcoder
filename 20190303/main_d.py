#20190303
class UnionFind():
    '''
    @properties
        parents:
            - 各要素の親要素の番号を格納するリスト
            - 要素が根の場合はそのグループの要素数を格納する
    '''
    def __init__(self,n):
        self.n = n 
        self.parents = [-1] * n
    def __str__(self):
        return '\n'.join('{}: {}'.format(r,self.members(r)) for r in self.roots())
    def find(self,x):
        if self.parents[x] < 0: #初期値の場合
            return x
        else:
            self.parents[x] = self.find(self.parents[x]) #どの根に紐づいているかを判断する
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x) #どの根に紐づいているかを判断する
        y = self.find(y) #どの根に紐づいているかを判断する
        if x == y: #同じ根に紐づいている場合は何もしない
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x] += self.parents[y] #根の個数を増やす。。？
        self.parents[y] = x #根を変更する
    def members(self,x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i,x in enumerate(self.parents) if x < 0 ]
    def weighted_roots_sizes(self):
        return [ self.size(i) for i,x in enumerate(self.parents) if x < -1 ]
    def size(self,x):
        return -self.parents[self.find(x)]
N,M = map(int,input().split(' '))
bridges = [ list(map(int,input().split(' '))) for _ in range(M) ]
uf = UnionFind(N)
base_num = N * (N-1) //2
output_list = [0]*(M+1)
output_list[M] = base_num
for i in reversed(range(M)):
    bridge_from = bridges[i][0] - 1
    bridge_to = bridges[i][1] - 1
    current_amount = 0
    if uf.find(bridge_from) == uf.find(bridge_to):
        output_list[i] = output_list[i+1]
        continue
    output_list[i] = output_list[i+1] - uf.size(bridge_from) * uf.size(bridge_to)
    uf.union(bridge_from,bridge_to)
for i in range(1,M+1):
    print(output_list[i])