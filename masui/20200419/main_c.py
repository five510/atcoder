N = int(input())
an = list(map(int,input().split(' ')))
cnt = 1
is_increased = True
is_init = True
for i in range(1,N):
    if is_init:
        if an[i] > an[i-1]:
            is_increased = True
        elif an[i] < an[i-1]:
            is_increased = False
        elif an[i] == an[i-1]:
            continue
        is_init = False
    else:
        if is_increased:
            if an[i] >= an[i-1]:
                continue
            else:
                is_init = True
                cnt +=1
        else:
            if an[i] <= an[i-1]:
                continue
            else:
                is_init = True
                cnt +=1
print(cnt)
