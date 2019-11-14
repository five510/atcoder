sx,sy,tx,ty = map(int,input().split(' '))

output_txt = ''

#1st txt
x1 = tx -sx
if x1 >0:
    txt_x1 = 'R' * x1
else:
    txt_x1 = 'L' * x1
y1 = ty -sy
if y1 >0:
    txt_y1 = 'U' * y1
else:
    txt_y1 = 'D' * y1

#2nd txt
if x1 >0:
    txt_x2 = 'L' * x1
else:
    txt_x2 = 'R' * x1
if y1 >0:
    txt_y2 = 'D' * y1
else:
    txt_y2 = 'U' * y1

#3rd txt
if y1 >0:
    txt_3 = 'D' 
else:
    txt_3 = 'U'

if x1 >0:
    txt_3 += 'R' * x1 + 'R'
else:
    txt_3 += 'L' * x1 + 'L'

if y1 >0:
    txt_3 += 'U' * y1 + 'U'
else:
    txt_3 += 'D' * y1 + 'D'

if x1 >0:
    txt_3 += 'L'
else:
    txt_3 += 'R'


#4th txt
if y1 >0:
    txt_4 = 'U' 
else:
    txt_4 = 'D'

if x1 >0:
    txt_4 += 'L' * x1 + 'L'
else:
    txt_4 += 'R' * x1 + 'R'

if y1 >0:
    txt_4 += 'D' * y1 + 'D'
else:
    txt_4 += 'U' * y1 + 'U'

if x1 >0:
    txt_4 += 'R'
else:
    txt_4 += 'L'

output_txt = txt_x1 + txt_y1 + txt_x2 + txt_y2
print(output_txt+txt_3+txt_4)