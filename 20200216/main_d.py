import bisect
N,K = map(int,input().split(' '))
An = list(map(int,input().split(' ')))
An.sort()
idx = bisect.bisect_left(An,0)
positive = An[idx:] 
negative = An[:idx]


max_candidate = 10**18 + 1
min_candidate = -1 * (10**18) - 1

while True:
    middle = (max_candidate + min_candidate)//2
    if 0 <= middle:
        current_length = len(positive) * len(negative)
        candidate_list = []
        #正 * 正
        for i,n1 in enumerate(positive):
            n2_list = positive[i+1:]
            if n1 != 0:
                n2_candidate = middle / n1
                n2_idx = bisect.bisect_right(n2_list,n2_candidate)
            else:
                n2_idx = len(n2_list)
            current_length += n2_idx
            if 0 < n2_idx:
                n2 = n2_list[n2_idx-1]
                candidate_list.append(n1 * n2)
            else:
                break
        #負 * 負
        for i,n1 in enumerate(negative):
            n2_list = negative[i+1:]
            n2_candidate = middle / n1
            n2_idx = bisect.bisect_right(n2_list,n2_candidate)
            if n2_idx < len(n2_list):
                current_length += len(n2_list) - n2_idx - 1
                n2 = n2_list[n2_idx-1]
                candidate_list.append(n1 * n2)
            else:
                break
    else:
        current_length = 0
        candidate_list = []
        #正 * 負
        for i,n1 in enumerate(negative): 
            n2_list = positive
            n2_candidate = middle / n1
            n2_idx = bisect.bisect_right(n2_list,n2_candidate)
            #current_length += n2_idx
            if n2_idx < len(n2_list):
                current_length += len(n2_list) - n2_idx
                n2 = n2_list[n2_idx-1]
                candidate_list.append(n1 * n2)
            else:
                break
    if min_candidate+1 == max_candidate:
        break
    if current_length == K:
        print(max(candidate_list))
        exit(0)
    elif current_length < K:
        min_candidate = middle
    else:
        max_candidate = middle
print(max(candidate_list))
