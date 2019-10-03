S = input()

divide_count = 0
previous_s = S[0]
current_s = ''
result = [S[0]]
s_len = len(S)

for i in range(1, s_len):
    current_s += S[i]
    if previous_s == current_s:
        continue
    else:
        result.append(current_s)
        previous_s = current_s
        current_s = ''  
print(len(result))