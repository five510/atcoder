N = int(input())
def f(a,count):
   a2 = 10**a
   if a2 <= N:
       if a % 2 == 1:
           count = count + a2 - (10**(a-1))
       return f(a+1,count)
   else:
       if a % 2 == 1:
           return count+ (N- (10**(a-1))) + 1
       else:
           return count
print(f(1,0))