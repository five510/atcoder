AB = input().split(' ')
A = int(AB[0])
B = int(AB[1])
if A > 9 or B > 9:
    print(-1)
else:
    print(A*B)