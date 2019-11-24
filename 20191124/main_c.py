A,B,X = map(int,input().split(' '))

max_num = 10**9 +1
l = 1
r = max_num
possible = 0
current_num = 0
while l + 1 <= r:
    m = (l + r)//2
    current_num = A*m + B*len(str(m))
    if current_num <= X:
        possible = max(possible,m)
        l = m +1
    else:
        r = m
print(possible)