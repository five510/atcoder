N = int(input())
'''
def factorization(n):
    arr = [1,1]
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            while temp%i==0:
                if arr[1] >= arr[0]:
                    arr[0] = arr[0]*i
                else:
                    arr[1] = arr[1]*i
                temp //= i   
    if temp!=1:
        if arr[1] >= arr[0]:
            arr[0] = arr[0]*temp
        else:
            arr[1] = arr[1]*temp
    if arr==[1,1]:
        arr[0] =n
    return arr

facro = factorization(N)
print(facro[0] +facro[1] -2)
'''
min_num = 1
 
for i in reversed(range(2,int(-(-N**0.5//1))+1)):
    if N%i == 0:
        #print(i)
        min_num = i
        break

print(min_num + N//min_num-2)