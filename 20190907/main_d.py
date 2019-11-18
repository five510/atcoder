N,K = map(int,input().split(' '))
S = input()
if S[0] == 'L':
    search_s = 'R'
    non_search_s = 'L'
else:
    search_s = 'L'
    non_search_s = 'R'
i = 0
new_S = ''
previous_s = S[0]
while K != 0 and i != N:
    if previous_s != S[i]:
        if previous_s == search_s:
            K -= 1
        previous_s = S[i]        
    i += 1
if K > 0:
    print(N-1)
else:
    new_S += non_search_s*(i-1)
    new_S += S[i-1:N]
    count_s = 0
    previous_s = new_S[0]
    for i in range(1,N):
        if previous_s == new_S[i]:
            count_s +=1
        else:
            previous_s = new_S[i]
    print(count_s)