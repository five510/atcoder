#import copy
N = int(input())
An = list(map(int,list(input())))
#print(An)
def solve(n):
    previous_num = -1
    previous_num = -1
    insert_idx = 0
    for i in range(n-1):
        current_num = abs(An[i]-An[i+1])
        if current_num == previous_num:
            continue
        An[insert_idx] = current_num
        previous_num = current_num
        insert_idx += 1
    if insert_idx == 1:
        An[1] = An[0]
    return insert_idx

def solve2(n):
    previous_num = -1
    previous_previous_num = -1
    insert_idx = 0
    for i in range(n-1):
        current_num = abs(An[i]-An[i+1])
        if current_num == previous_num and previous_num == previous_previous_num:
            continue
        An[insert_idx] = current_num
        previous_previous_num = previous_num
        previous_num = current_num
        insert_idx += 1
    if insert_idx == 1:
        An[1] = An[0]
    return insert_idx
An2 = [-1]*N
start_idx = -1
is_sec = False
for i in range(N):
    if An[i] == 1 and start_idx == -1:
        start_idx = i
        expected = 3
        expected_seconde = 3
    if start_idx > 0:
        if expected == 3 and An[i] == expected and is_sec:
            expected = 0
        elif expected == 3 and An[i] == expected and is_sec:
            
current_n = N
while 2 < current_n:
    current_n = solve2(current_n)
print(abs(An[1]-An[0]))