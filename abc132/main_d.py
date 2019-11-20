N,K = map(int,input().split(' '))
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 10**9+7 #出力の制限
max_N = 2000 #階乗の制限どれだけ
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
for i in range( 2, max_N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
base_num = N-K+1
for i in range(K):
    select_num = cmb(base_num,i+1,mod)
    seq_num = cmb(K-1,i,mod)
    count_n = (select_num*seq_num)%mod
    print(count_n)