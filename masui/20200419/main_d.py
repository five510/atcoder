N = int(input())
rests =  [list(map(int,input().split('/'))) for _ in range(N)]
def calendar():
    calendar_list = []
    youbi = 1
    def next_youbi(y):
        if y == 7:
            return 1
        else:
            return y + 1
    for i in range(1,13):
        if i == 2:
            day = 29
        elif i == 4 or i == 6 or i == 9 or i == 11:
            day = 30
        else:
            day = 31
        month = []
        for m in range(day):
            month.append(youbi)  # 1 ~ 7の曜日 1 == sun
            youbi = next_youbi(youbi)
        calendar_list.append(month)
    return calendar_list

def is_rest(y):
    return y == 1 or y >= 7

calendar_list = calendar()
for rest in rests:
    month = rest[0] - 1
    day = rest[1] - 1 
    should_insert = True
    while should_insert:
        y = calendar_list[month][day]
        if not is_rest(y):
            calendar_list[month][day] = 8
            break
        if day == len(calendar_list[month]) -1:
            if month == 11:
                break
            month += 1
            day = 0
        else:
            day += 1
max_rest = 0
tmp_rest = 0
for m in range(12):
    for d in range(len(calendar_list[m])):
        y = calendar_list[m][d]
        if is_rest(y):
            tmp_rest += 1
        else:
            max_rest = max(max_rest,tmp_rest)
            tmp_rest = 0
print(max(max_rest,tmp_rest))
