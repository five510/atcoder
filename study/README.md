## listの処理

### 特定の要素数を生成したい場合

```
hoge_list = [0] * N
```

### 合計値を取りたい時

```
>>> hoge = [1,2,3,4,5]
単純な合計値
>>> sum(hoge)
15
1 --> 4までの合計値
>>> sum(hoge[1:4])
9
1,3個目の要素(2の倍数の要素)
>>> sum(hoge[1::2])
6
```

### 逆さから処理したい時

```
>>> range(5)
[0, 1, 2, 3, 4]
>>> hoge = range(5)
>>> hoge.reverse()
>>> hoge
[4, 3, 2, 1, 0]
```

### 特定の場所に要素を入れたい時

```
>>> hoge
[4, 3, 2, 1, 0]
>>> hoge.insert(0,'hoge')
>>> hoge
['hoge', 4, 3, 2, 1, 0]
```

けどfor文で `hoge.insert(0,'hoge')`を文回すのはご法度。

`hoge.append('hoge')`をしたのちに `hoge.reverse()`をする

## 最小値を求めたい場合

- `import heapq`を使う。優先度キューっていうらしい
  - `heappush`で要素の格納
  - `heappop` で要素の取り出し + 削除が可能
```
>>> import heapq
>>> heapq.heappush(fuga,1)
>>> heapq.heappush(fuga,2)
>>> heapq.heappush(fuga,3)
>>> heapq.heappop(fuga)
1
>>> heapq.heappop(fuga)
2
>>> heapq.heappop(fuga)
3
```

### 最大値を求めたい時

- ちょっと面倒。`heapq`は最小値の取り出しのみサポートしているので、常に要素に対して * (-1)をすると上手くいく
```
>>> fugaaa = []
>>> heapq.heappush(fugaaa,-1)
>>> heapq.heappush(fugaaa,-2)
>>> heapq.heappush(fugaaa,-3)
>>> heapq.heappop(fugaaa) * (-1) #取り出す時も * (-1)
3
```

## 動的計画法 (Dynamic Programming, DP)

https://qiita.com/drken/items/a5e6fe22863b7992efdb

```py
dp = [0]
def dynamic_programing(An):
    for i in range(An):
        dp[i+1] = max(dp[i],dp[i]+An[i])
```


## 最大公約数の求め方
```py
def gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)
```