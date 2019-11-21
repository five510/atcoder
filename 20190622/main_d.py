N = int(input())
ABn = [ list(map(int,input().split(' '))) for _ in range(N) ]
ABn.sort(key=lambda x: x[1])
count_time = 0
for AB in ABn:
    count_time += AB[0]
    if count_time <= AB[1]:
        continue
    else:
        print('No')
        exit()
print('Yes')