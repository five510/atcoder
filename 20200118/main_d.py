N = int(input())
An = list(map(int,input().split(' ')))
Bn = list(map(int,input().split(' ')))
cnt = 0


def detect_min_value(start_an_idx,thred_value):
    belong = ''
    idx = 0
    min_number = 10**9
    while start_an_idx < N:
        if thred_value <= An[start_an_idx] < min_number:
            min_number = An[start_an_idx]
            belong = 'a'
            idx = start_an_idx
        if start_an_idx == N-1:
            break
        if thred_value <= Bn[start_an_idx+1] < min_number:
            min_number = Bn[start_an_idx+1]
            belong = 'b'
            idx = start_an_idx + 1
        start_an_idx += 2
    return belong,idx,min_number

def change_value(an_idx,replace_an_idx,cnt):
    for r_i in reversed(range(an_idx+1,replace_an_idx+1)):
           tmp = An[r_i]
           An[r_i] = Bn[r_i-1]
           Bn[r_i-1] = tmp

           tmp = An[r_i-1]
           An[r_i-1] = Bn[r_i]
           Bn[r_i] = tmp
    cnt += (replace_an_idx-an_idx)
    return cnt

for i in range(N):
    if i != 0:
        belong,replace_idx,min_number = detect_min_value(i,An[i-1])
    else:
        belong,replace_idx,min_number = detect_min_value(i,0)
    cnt = change_value(i,replace_idx,cnt)

min_value = (10**9 +7)*(-1)
for a in An:
    if min_value <= a:
        min_value = a
        continue
    else:
        print(-1)
        exit(0)
print(cnt)