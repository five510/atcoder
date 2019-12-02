X = input()

last2 = int(X[len(X)-2:])
try_num = int(X) //100

for i in range(try_num):
    if last2 > 5:
        last2 -= 5
    else:
        print(1)
        exit(0)
print(0)