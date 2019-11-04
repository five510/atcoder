NM = input().split(' ')
N = int(NM[0])
M = int(NM[1])
#先にソートするのが,二部探索において大切
Pn = [ int(input()) for _ in range(N)]
Pn.append(0)
Pn.sort()

'''
#全探索
candidate_s = 0
max_candidate_s = 0
for i1 in range(len(Pn)):
    for i2 in range(len(Pn)):
        for i3 in range(len(Pn)):
            for i4 in range(len(Pn)):
                candidate_s = Pn[i1] + Pn[i2] + Pn[i3] + Pn[i4]
                if candidate_s <= M and max_candidate_s < candidate_s:
                    max_candidate_s = candidate_s
print(max_candidate_s)



#N^3logN
max_candidate_s = 0
for i1 in range(len(Pn)):
    for i2 in range(len(Pn)):
        for i3 in range(len(Pn)):
            l = 0
            r = len(Pn) - 1
            candidate_p4 = 0
            if (Pn[i1] + Pn[i2] + Pn[i3]) > M: #例外処理
                continue
            while l + 1 <= r:
                m = (l + r)//2
                # Pn[i4] = M - Pn[i1] - Pn[i2] - Pn[i3]を前提に考える
                if Pn[m] > (M - Pn[i1] - Pn[i2] - Pn[i3]): #基準値より大きい場合
                    r = m
                else: #基準値より小さい場合
                    if candidate_p4 < Pn[m]:
                        candidate_p4 = Pn[m]
                    l = m + 1 #次回mを含む必要がないので m +1とする
            if max_candidate_s < candidate_p4 + Pn[i1] + Pn[i2] + Pn[i3]:
                max_candidate_s = candidate_p4 + Pn[i1] + Pn[i2] + Pn[i3]
print(max_candidate_s)
'''

'''
#N^2logN^2 + N^2 
max_candidate_s = 0
#先にN^2で全列挙
all_pn2_candidate = []
for i1 in range(len(Pn)):
    for i2 in range(len(Pn)):
        all_pn2_candidate.append(Pn[i1] + Pn[i2])
all_pn2_candidate.sort()

for i1 in range(len(Pn)):
    for i2 in range(len(Pn)):
        l = 0
        r = len(all_pn2_candidate) - 1
        candidate_pn34 = 0
        if (Pn[i1] + Pn[i2]) > M: #例外処理
            continue
        while l + 1 <= r:
            m = (l + r)//2
            # Pn[i4] = M - Pn[i1] - Pn[i2] - Pn[i3]を前提に考える
            if all_pn2_candidate[m] > (M - Pn[i1] - Pn[i2]): #基準値より大きい場合
                r = m
            else: #基準値より小さい場合
                if candidate_pn34 < all_pn2_candidate[m]:
                    candidate_pn34 = all_pn2_candidate[m] 
                l = m + 1 #次回mを含む必要がないので m +1とする
        if max_candidate_s < candidate_pn34 + Pn[i1] + Pn[i2]:
            max_candidate_s = candidate_pn34 + Pn[i1] + Pn[i2]
print(max_candidate_s)
'''

'''
max_candidate_s = 0
#先にN^2で全列挙
all_pn2_candidate = []
for i1 in range(len(Pn)):
    for i2 in range(i1,len(Pn)):
        all_pn2_candidate.append(Pn[i1] + Pn[i2])
all_pn2_candidate.sort()

for i in range(len(all_pn2_candidate)):
    l = i
    r = len(all_pn2_candidate) - 1
    candidate_pn34 = 0
    if (all_pn2_candidate[i]) > M: #例外処理
        continue
    while l + 1 <= r:
        m = (l + r)//2
        # Pn[i4] = M - Pn[i1] - Pn[i2] - Pn[i3]を前提に考える
        if all_pn2_candidate[m] > (M - all_pn2_candidate[i]): #基準値より大きい場合
            r = m
        else: #基準値より小さい場合
            if candidate_pn34 < all_pn2_candidate[m]:
                candidate_pn34 = all_pn2_candidate[m] 
            l = m + 1 #次回mを含む必要がないので m +1とする
    if max_candidate_s < candidate_pn34 + all_pn2_candidate[i]:
        max_candidate_s = candidate_pn34 + all_pn2_candidate[i]
print(max_candidate_s)
'''

#N^2logN^2 + N^2 ギリギリ 1.5s以下
from bisect import bisect_right

max_candidate_s = 0
#先にN^2で全列挙
all_pn2_candidate = []
for i1 in range(len(Pn)):
    for i2 in range(len(Pn)):
        all_pn2_candidate.append(Pn[i1] + Pn[i2])
all_pn2_candidate.sort()

for i in range(len(all_pn2_candidate)):
    if (all_pn2_candidate[i]) > M: #例外処理
        continue
    insert_index = bisect_right(all_pn2_candidate,M - all_pn2_candidate[i])
    temp_ans = all_pn2_candidate[insert_index-1]
    if max_candidate_s < temp_ans + all_pn2_candidate[i]:
        max_candidate_s = temp_ans + all_pn2_candidate[i] 

print(max_candidate_s)
