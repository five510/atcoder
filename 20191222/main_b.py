N = int(input())
S,T = map(str,input().split(' '))
output = ''
for i in range(N):
    output += S[i]
    output += T[i]
print(output)