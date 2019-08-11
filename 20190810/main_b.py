kx = input()
k = int(kx.split(' ')[0])
x = int(kx.split(' ')[1])

output_list = []

for i in range(1,k):
    output_list.append(x-(k-i))
output_list.append(x)
for i in range(1,k):
    output_list.append(x+i)
print(' '.join(map(str,output_list)))