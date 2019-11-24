X,Y = map(int,input().split(' '))

count_sum = 0

def count_money(X,count_sum):
    if X == 1:
        count_sum += 300000
    elif X ==2:
        count_sum += 200000
    elif X ==3:
        count_sum += 100000
    return count_sum

count_sum = count_money(X,count_sum)
count_sum = count_money(Y,count_sum)
if X == 1 and Y ==1:
    count_sum += 400000
print(count_sum)