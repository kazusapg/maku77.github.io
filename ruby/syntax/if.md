---
title: "Ruby の制御構文 -- if と unless による分岐"
date: "2002-08-20"
---

if の構文
====
```ruby
if 条件
  文1
elsif
  文2
else
  文3
end
```

Ruby の `if` 文は式として評価することができるので、次のように代入文と組み合わせて使用することもできます。

```ruby
str = if x == 1
        "みかん"
      elsif x == 2
        "バナナ"
      else
        "りんご"
      end
```

上記の例では、`x == 1` が成立するとき、`str` 変数に "みかん" が代入されます。


unless の構文
====

Ruby には、`if not` の省略系として `unless` が用意されています。
ただし、`unless` の場合は、`elsif` で条件をつなげていくことはできません。

```ruby
unless 条件
  文1
else
  文2
end
```

