N = int(input())
for i in range(N):
  X, Y, S = map(str,input().split(' '))
  X = int(X)
  Y = int(Y)
  cost = 0
  # CJ -> X
  # JC -> Y
  previous = S[0]
  for i2 in range(1, len(S)):
    current = S[i2]
    if current != '?' and previous != current:
      if previous + current == 'CJ':
        cost += X
      if previous + current == 'JC':
        cost += Y
      previous = current
  print(f"Case #{str(i+1)}: {str(cost)}")