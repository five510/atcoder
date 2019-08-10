ab = input()
a = int(ab.split(' ')[0])
b = int(ab.split(' ')[1])

if (a+b)%2 == 0:
   print(int((a+b)/2))
else:
   print('IMPOSSIBLE')