N = int(input())
min_list = []
for _ in range(N):
    w = int(input())
    flag = True
    min_list.sort()
    for idx,m in enumerate(min_list):
        if m >= w:
            min_list[idx] = w
            flag = False
            break
    if flag:
        min_list.append(w)
print(len(min_list))