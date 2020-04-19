N,K = map(int,input().split(' '))
diff = N % K
print(min(K-diff,diff)) 