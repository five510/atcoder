S = input()

loop_num = len(S) // 2
output_count = 0
for i in range(loop_num):
    if S[i] != S[len(S)-i-1]:
        output_count += 1
print(output_count)