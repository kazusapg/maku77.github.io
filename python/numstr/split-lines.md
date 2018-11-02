---
title: "文字列を改行で分割して一行ずつのリストにする (splitlines)"
date: "2012-09-28"
---

改行コード (`\n`, `\r`, `\r\n`) を含む文字列を行ごとのリストに分割するには、`splitlines` メソッドを使用します。

#### 文字列を改行で分割する

~~~ python
s = "AAA\nBBB\nCCC"
lines = s.splitlines()  #=> ['AAA', 'BBB', 'CCC']
lines = s.splitlines(True)  #=>  ['AAA\n', 'BBB\n', 'CCC'] （改行を残す）
~~~

改行の前後のスペース等は削除されないので、必要に応じて `strip` を組み合わせて使用してください。

~~~
s = "AAA  \n  BBB  \n  CCC  "
lines = s.splitlines()  #=> ['AAA  ', '  BBB  ', '  CCC  ']
lines = [x.strip() for x in s.splitlines()]  #=> ['AAA', 'BBB', 'CCC']
~~~

`split('\n')` を使用しても同様に改行で分割できるように見えますが、改行コードとして CR+LF (`\r\n`) を含んでいたりするとうまく分割できません。
`splitlines` であれば、LF(`\n`)、CR(`\r`)、CR+LF(`\r\n`) で分割してくれるので、プラットフォームに依存しない実装を行えます。

~~~
s = "AAA\nBBB\rCCC\r\nDDD"
lines = s.split('\n')   #=> ['AAA', 'BBB\rCCC\r', 'DDD']
lines = s.splitlines()  #=> ['AAA', 'BBB', 'CCC', 'DDD']
~~~

文字列を改行で分割するときは `split('\n')` を使用せず、`splitlines()` を使用してください。

