first = input()
second = input()
count = 0
for i in range(3):
    if first[i] == second[i]:
        count += 1
print(count)