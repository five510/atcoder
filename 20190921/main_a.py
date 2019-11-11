HWAB = input().split(' ')
H = int(HWAB[0])
W = int(HWAB[1])
A = int(HWAB[2])
B = int(HWAB[3])

sHW = []
inmpossible_flag = False
empty = 0
hcount = [0 for _ in range(W)]
for hi in range(H):
    next_w_list = [0 for _ in range(W)]
    if empty + A >= W:
        try:
            for i in range(W - A):
                next_w_list[empty + i] = 1
                hcount[empty + i] += 1
        except:
            inmpossible_flag = True
    else:
        for i in range(A):
            next_w_list[empty + i] = 1
            hcount[empty + i] += 1
    if inmpossible_flag:
        break
    if hcount[empty] == B:
        empty += A
    sHW.append(next_w_list)

# check High
for c in hcount:
    if not H - c == B and not c == B:
        inmpossible_flag = True
        break

if inmpossible_flag:
    print('No')
else:
    for n in sHW:
        print(''.join(map(str,n)))
    
'''
def regressive_change(hi,wi):
    if W == wi +1:
        return False
    if sHW[hi][wi+1] == 1:
        return regressive_change(hi,wi+1)
    else:
        sHW[hi][wi+1] = 1
        return True

for wi in range(W):
    one_count = 0
    for hi in range(H):
        if sHW[hi][wi] == 1:
            one_count += 1
            if one_count > B:
                flag = regressive_change(hi,wi)
                if not flag:
                    break
                sHW[hi][wi] = 0
                one_count -= 1
                    
    if not H - one_count == B and not one_count == B:
        inmpossible_flag = True
        break
    
if inmpossible_flag:
    print('No')
else:
    for n in sHW:
        print(''.join(map(str,n)))
'''
