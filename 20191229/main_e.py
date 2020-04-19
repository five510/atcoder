N,M = map(int,input().split(' '))
An =list(map(int,input().split(' ')))
#An.sort(reverse=True)

all_list = []
for i,a in enumerate(An):
    all_list.append(a+a)
    for a2 in An[i+1:]:
        all_list.append(a+a2)
        all_list.append(a+a2)
    
all_list.sort(reverse=True)
print(sum(all_list[:M]))
