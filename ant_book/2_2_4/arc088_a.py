X,Y = map(int,input().split(' '))
output_list = []
while X <= Y:
    output_list.append(X)
    X = X*2
print(len(output_list))
