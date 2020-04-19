S = input()
half_l = int((len(S) -1)/2)
mae = S[0:half_l]
ato = S[half_l+1:len(S)]

start = int((len(S) +3)/2)
target_str = S[start-1:len(S)]

def ispalindrome(str): return True if str == str[::-1] else False

if not ispalindrome(S):
    print('No')
    exit(0)

if not ispalindrome(mae):
    print('No')
    exit(0)

if not ispalindrome(target_str):
    print('No')
    exit(0)
print('Yes')

