N = int(input())
An = list(map(int,input().split(' ')))
emploees = [0]*N
for i in range(N-1):
    emploees[An[i]-1] += 1
for e in emploees:
    print(e)