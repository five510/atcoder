N = int(input())
S = list(input())

dp = [ [0]*10 for _ in range(10) ]

all_count = 0
for first_num in range(10):
    for second_num in range(10):
        cache = []
        is_first = False
        is_second = False
        for i in range(N):
            target = int(S[i])
            if target == first_num and not is_first:
                is_first = True
                continue
            if is_first and target == second_num and not is_second:
                is_second = True
                continue
            if is_first and is_second:
                #print(first_num,second_num,target)
                if not target in cache:
                    all_count +=1
                    cache.append(target)
print(all_count)

