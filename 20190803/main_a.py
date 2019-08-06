abc = input()
a = int(abc.split(' ')[0])
b = int(abc.split(' ')[1])
c = int(abc.split(' ')[2])
if (c-(a-b))>0:
   print(c-(a-b))
else:
   print(0)