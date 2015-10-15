---
title: 文字列から正規表現にマッチする部分を取り出す
created: 2011-07-29
layout: ruby
---

ある文字列リテラル、あるいは文字列変数の中から、正規表現に一致する部分文字列を抽出するには、`String#slice(Regexp)` を使用できます。

```ruby
m = 'abcdefg'.slice(/c.+/)
puts m   #=> "cdefg"
```

正規表現に一致する文字列が見つからない場合は、`slice` メソッドは `nil` を返します。
