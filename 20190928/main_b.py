NK = input().split(' ')
N = int(NK[0])
K = int(NK[1])
Hn = list(map(int,input().split(' ')))

count = 0
for h in Hn:
    if h >= K:
        count += 1
print(count)