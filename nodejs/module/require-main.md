---
title: "モジュール自身のコードにテストコードを記述する (require.main)"
date: "2018-12-10"
---

Node.js で実行中のプログラムから `require.main` を参照すると、エントリポイントとして起動した `module` インスタンスを参照することができます。
つまり、下記のようにして、エントリポイントとして起動された JavaScript ファイルかどうかを判別することができます。

~~~ javascript
if (require.main === module) {
  // このモジュールを node で直接起動した場合のみ実行される
}
~~~

あるいは、下記のように判定することもできます。

~~~ javascript
if (require.main.filename === __filename) {
  // ...
}
~~~

この仕組みを利用して、あるモジュールのテストコードを、そのモジュールのコード内に埋め込むことができます。
下記は、`add` 関数と `subtract` 関数を提供する簡単なモジュールのサンプルです。

#### mymath.js

~~~ javascript
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = {
  add: add,
  subtract: subtract
};

// このモジュール自身のテストコード
if (require.main === module) {
  let assert = require('assert');
  assert.equal(add(1, 2), 3);
  assert.equal(subtract(1, 2), -1);
}
~~~

末尾に記述されているテストコードは、下記のように直接モジュールを起動することで実行できます。

~~~
$ node mymath.js
~~~

逆に、他の JavaScript コードからこのモジュールをロードする場合は、テストコードの部分は実行されません。

#### main.js

~~~ javascript
var mymath = require('./mymath');  // テストコードは実行されない
console.log(mymath.add(100, 50));  // => 150
~~~

