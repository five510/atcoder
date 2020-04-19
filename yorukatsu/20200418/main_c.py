N = int(input())
Sn = [ ''.join(sorted(input())) for _ in range(N)]
Sn_key = {}
for s in Sn:
    if s not in Sn_key:
        Sn_key[s] = 1
    else:
        Sn_key[s] += 1
cnt = 0

for v in Sn_key.values():
    if v >= 2:
        cnt += v * (v-1) // 2
print(cnt)