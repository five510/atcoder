Na,Nb = map(int,input().split(' '))

An = list(map(int,input().split(' ')))
Bn = list(map(int,input().split(' ')))

count_map = {}
only_b_count = 0
dupulicate_count = 0
for val in An:
    count_map[val] = 1

for val in Bn:
    if val in count_map:
        dupulicate_count += 1
    else:
        only_b_count +=1
print(dupulicate_count/(len(An)+only_b_count))