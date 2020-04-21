import copy
N = int(input())
Dn = list(map(int,input().split(' ')))
d_map = {}
for d in Dn:
    if d not in d_map:
        d_map[d] = 1
    else:
        d_map[d] += 1
if 0 in d_map:
    print(0)
    exit(0)
if len(Dn) == 1:
    print(Dn[0])
    exit(0)
for v in d_map.values():
    if 3 <= v:
        print(0)
        exit(0)
all_combination = [ [0] ]
for k,v in d_map.items():
    if v == 1:
        len_all_combination = len(all_combination)
        for i in range(len_all_combination):
            tmp = copy.deepcopy(all_combination[i])
            all_combination[i].append(k)
            tmp.append(24-k)
            all_combination.append(tmp)
    else:
        for comb in all_combination:
            comb.append(k)
            comb.append(24-k)
ans = -1
for comb in all_combination:
    comb.sort()
    #print(comb)
    tmp = 100
    for i in range(1,len(comb)):
        if comb[i] > 12:
            tmp = min(tmp,min(comb[i]-comb[i-1],24-comb[i]))
        else:
            tmp = min(tmp,comb[i]-comb[i-1])
    ans = max(ans,tmp)
print(ans)