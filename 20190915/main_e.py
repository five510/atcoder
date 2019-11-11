N = int(input())
S =  input()
n_list = [0] * N
max_length = 0
max_reach = -1
for i in range(N):
    if i < max_reach:
        continue
    for j in range(i+max_length,N):
        if S[i:j] in S[j:N]:
            continue
        else:
            if j == i+max_length:
                break
            elif j > max_length:
                max_length = j-i-1
                max_reach = j-i-1
                break
print(max_length)