Sn = input().split('+')
count = 0
for val in Sn:
    if not '0' in val:
        count += 1
print(count)