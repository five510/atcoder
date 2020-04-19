import math
N,M = map(int,input().split(' '))
name = input()
kit = input()

alpahebet_list = [chr(ord('a') + i) for i in range(26)]
alpahebet_dict = {}
for v in alpahebet_list:
    alpahebet_dict[v.upper()] = 0

use_alpahebet_dict = {}
for v in alpahebet_list:
    use_alpahebet_dict[v.upper()] = 0

for i in range(M):
    alpahebet_dict[kit[i]] += 1
for i in range(N):
    if alpahebet_dict[name[i]]== 0:
        print(-1)
        exit(0)
    else:
        use_alpahebet_dict[name[i]] +=1
ans = 0
for k,v in use_alpahebet_dict.items():
    if v == 0:
        continue
    ans = max(ans,math.ceil(v/alpahebet_dict[k]))
print(ans)
