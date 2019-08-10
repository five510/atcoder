N = int(input())
An1 = input().split(' ')
Bn = input().split(' ')

next_add = 0
attacked = 0
for i in range(N):
    me = int(Bn[i])
    enemy = int(An1[i])
    if next_add > 0:
        diff1 = next_add - enemy
        if diff1 < 0:
            attacked = attacked + next_add
            enemy = enemy -next_add
            next_add = 0
        else:
            attacked = attacked + enemy
            next_add = me
            continue
        
    diff2 = me - enemy
    if diff2 < 0:
        attacked = attacked + me
        next_add = 0
    else:
        attacked = attacked + enemy
        next_add = diff2

if next_add > 0:
    enemy = int(An1[N])
    diff1 = next_add - enemy
    if diff1 < 0:
        attacked = attacked + next_add
    else:
        attacked = attacked + enemy
print(attacked)