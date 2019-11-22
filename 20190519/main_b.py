S = input()
front = int(S[0:2])
back = int(S[2:4])
if 1 <= front <= 12 and 1 <= back <= 12:
    print('AMBIGUOUS')
elif 0 <= front <= 99 and 1 <= back <= 12:
    print('YYMM')
elif 1 <= front <= 12 and 0 <= back <= 99:
    print('MMYY')
else:
    print('NA')