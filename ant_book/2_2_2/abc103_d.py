N,M = map(int,input().split(' '))
sections = [list(map(int,input().split(' '))) for _ in range(M) ]

'''
tmp_list = [sections[0]]
for i in range(1,len(sections)):
    for j in range(i):
        if sections[i] < tmp_list[j]:
            tmp_list.insert(j,sections[i])
            break
        if j == i -1:
            tmp_list.append(sections[i])
'''
min_end = 10000000000000000
sorted_list = sorted(sections)
cnt = 0
for section in sorted_list:
    if min_end <= section[0]:
        cnt += 1
        min_end = min_end = 10000000000000000
    min_end = min(min_end,section[1])
cnt += 1
print(cnt)
