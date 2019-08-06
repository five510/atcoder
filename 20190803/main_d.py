import sys
sys.setrecursionlimit(1000000000)
char = list(input())
char_list_num = len(char)
count_list = [0] * char_list_num

def f(first_char,n,add_num):
    if first_char == char[n+add_num] and n + add_num != char_list_num - 1:
        return f(first_char,n+add_num,add_num)
    else:
        return n+add_num

num = 0
while not num == char_list_num - 1:
    reach_loop_num = f(char[num],num,1)
    diff = reach_loop_num - num
    if reach_loop_num == char_list_num - 1:
        if char[num] == char[reach_loop_num]:
            diff += 1
        else:
            count_list[reach_loop_num] += 1
    if char[num] == 'R':
        if diff % 2 == 0:
            count_list[reach_loop_num] += diff//2
            count_list[reach_loop_num-1] += diff//2
        else:
            count_list[reach_loop_num] += diff//2
            count_list[reach_loop_num-1] += diff//2 +1
    else:
        if diff % 2 == 0:
            count_list[num] += diff//2
            count_list[num-1] += diff//2
        else:
            count_list[num] += diff//2 +1
            count_list[num-1] += diff//2
    num = reach_loop_num
print(' '.join(map(str,count_list)))