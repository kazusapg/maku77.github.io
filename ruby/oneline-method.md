---
title: "関数を一行で定義する"
date: "2011-10-01"
---

各行をセミコロンでつなげば、関数を一行で定義できます。

```ruby
def add(a,b); a+b; end
```

プログラミングコンテストなどで、コードを短く書きたい場合にマクロ風に使うと便利です。

```ruby
def readInt; gets.chomp.to_i; end
def readInts; gets.chomp.split.map(&:to_i); end
```

