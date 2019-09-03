N = int(input())
Hn = input().split(' ')
Hn.reverse()
max_map = (0,0)
count = 0
for i in range(len(Hn) -1):
    preh = int(Hn[i])
    posth = int(Hn[i+1])
    if posth >= preh:
        count += 1
        if (len(Hn) -1) == (i+1):
            if count > max_map[0]:
                max_map = (count, i +1)
    else:
        if count > max_map[0]:
            max_map = (count, i +1)
        count = 0

print(max_map[0])