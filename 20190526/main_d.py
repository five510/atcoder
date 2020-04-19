N,K= map(int,input().split(' '))
Vn_nomal = list(map(int,input().split(' ')))

Vn_reverse = list(reversed(Vn_nomal))

Vn_nomal_s = [Vn_nomal[0]]
Vn_reverse_s = [Vn_reverse[0]]
for i in range(1,len(Vn_nomal)):
    Vn_nomal_s.append(Vn_nomal_s[i-1]+Vn_nomal[i])
for i in range(1,len(Vn_reverse)):
    Vn_reverse_s.append(Vn_reverse_s[i-1]+Vn_reverse[i])
print(Vn_nomal_s)
print(Vn_reverse_s)

max_num = 0
current_sum = 0
for i in range(K):
    if 1 <= K-i-1:
        current_sum += Vn_nomal_s[K-i-1]
    
    if 1 <= i:
        current_sum += Vn_reverse_s[i-1]
    max_num = max(max_num,current_sum)
    current_sum = 0
print(max_num)