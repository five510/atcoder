N = int(input())
An = input().split(' ')

reach_num = 0
for a in An:
    if int(a) == reach_num + 1:
        reach_num += 1
if reach_num == 0:
    print(-1)
else:
    print(N - reach_num)