N = int(input())
S = input()

def solve(s,K):
    alpha2num = lambda s: ord(s) - ord('A') + 1
    num2alpha = lambda num: chr(num+64)
    num  = alpha2num(s)
    try_num = (num+K)%26
    if try_num == 0:
        try_num = 26
    alpha = num2alpha(try_num)
    return alpha
output = []
for i in range(len(S)):
    output.append(solve(S[i],N))
print(''.join(output))