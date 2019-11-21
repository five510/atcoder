S = input()
for i in  range(1,len(S)):
    if S[i-1] == S[i]:
        print('Bad')
        exit()
print('Good')