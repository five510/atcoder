# -*- coding: utf-8 -*-
T = int(input())

def reverse(l):
  list_len = len(l)
  tmp = [ 0 for _ in range(list_len) ]
  for i in range(list_len):
    tmp[i] = l[list_len - i - 1]
  return tmp

for i in range(T):
    N = int(input())
    Li = list(map(int,input().split(' ')))
    cost = 0
    for i2 in range(N - 1):
      sub_list = Li[i2:N]
      j = i2 + sub_list.index(min(sub_list))
      zero_to_i2_list = Li[0:i2]
      i2_to_j_list = Li[i2:j+1]
      reversed_i2_to_j_list = reverse(i2_to_j_list)
      j_to_n_lsit = Li[j+1:N]
      cost = cost + (j - i2 + 1)
      Li = zero_to_i2_list + reversed_i2_to_j_list + j_to_n_lsit
    print(f"Case #{str(i+1)}: {str(cost)}")