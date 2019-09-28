AB = input().split(' ')
A = int(AB[0])
B = int(AB[1])
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)
max_gcd = gcd(A,B)
result = factorization(max_gcd)
if len(result) == 1 and result[0][0] == 1:
    print(1)
else:
    print(len(result)+1)