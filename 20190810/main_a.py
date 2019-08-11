ab = input()
a = int(ab.split(' ')[0])
b = int(ab.split(' ')[1])

apb = a+b
amb = a-b
akb = a*b

if apb > amb:
    if apb > akb:
        print(apb)
    else:
        print(akb)
else:
    if amb > akb:
        print(amb)
    else:
        print(akb)