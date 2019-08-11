import math
N = int(input())
sorted_map = {}

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(N):
    inserted_flag = True
    input_sorted = ''.join(sorted(input()))
    if input_sorted in sorted_map.keys():
        sorted_map[input_sorted] += 1
        inserted_flag = False
    if inserted_flag:
        sorted_map[input_sorted] = 1

count = 0
for count_num in sorted_map.values():
    if count_num == 1:
        continue
    count += combinations_count(count_num, 2)
print(count)