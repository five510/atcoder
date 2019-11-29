S = input()
sequence = 0
max_sequence = 0
for i in range(len(S)):
    if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
        sequence += 1
    else:
        max_sequence = max(sequence,max_sequence)
        sequence = 0
max_sequence = max(sequence,max_sequence)
print(max_sequence)
