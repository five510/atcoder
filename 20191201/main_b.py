N = int(input())

for i in range(50000):
    if i * 108 //100 == N:
        print(i)
        exit(0)
print(':(')