import itertools

def reverse(l):
  list_len = len(l)
  tmp = [ 0 for _ in range(list_len) ]
  for i in range(list_len):
    tmp[i] = l[list_len - i - 1]
  return tmp

T = int(input())
for i in range(T):
  N, C = map(int,input().split(' '))
  lis = list(range(1,N+1))
  combinations = list(itertools.permutations(lis, N))
  flag = True
  for comb in combinations:
    n = len(comb)
    Li = list(comb)
    cost = 0
    for i2 in range(n - 1):
      sub_list = Li[i2:N]
      j = i2 + sub_list.index(min(sub_list))
      zero_to_i2_list = Li[0:i2]
      i2_to_j_list = Li[i2:j+1]
      reversed_i2_to_j_list = reverse(i2_to_j_list)
      j_to_n_lsit = Li[j+1:N]
      cost = cost + (j - i2 + 1)
      Li = zero_to_i2_list + reversed_i2_to_j_list + j_to_n_lsit
    if cost == C:
      print(f"Case #{str(i+1)}: {' '.join(map(str, comb))}")
      flag = False
      break
  if flag:
    print(f"Case #{str(i+1)}: IMPOSSIBLE")