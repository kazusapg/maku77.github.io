---
title: 関数内からしか参照できないプライベート関数を定義する
created: 2012-11-07
---

JavaScript では関数定義（関数リテラル）の中で、入れ子で関数を定義することができます。
JavaScript には関数スコープという概念があるので、入れ子の形で定義された関数は、外側からからアクセスできないプライベート関数になります。

```javascript
function convert(num) {
  for (var i = 0; i < 3; ++i) {
    num = square(num);
  }
  return num;

  function square(a) {
    return a * a;
  }
}

print(convert(2));  //=> 256
```

上記の例では、`square()` 関数は、`convert()` 関数の中からしか参照できません。

