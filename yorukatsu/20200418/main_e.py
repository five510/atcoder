import math
from collections import deque
N,D,A = map(int,input().split(' '))
XHn = [ list(map(int,input().split(' '))) for _ in range(N)]
ans = 0
XHn.sort()
attacks = deque([]) # (区間,攻撃回数)
attack = 0
ans = 0
for i  in range(N):
    x = XHn[i][0]
    h = XHn[i][1]
    while len(attacks) > 0 and x > attacks[0][0]:
        distance,attack_num = attacks.popleft()
        attack -= attack_num*A
    if h > attack:
        diff = h - attack 
        distance_attack = x + D*2
        need_attack = math.ceil(diff/A)
        attacks.append((distance_attack,need_attack))
        attack += A*need_attack
        ans += need_attack
print(ans)