---
title: HTML 要素に独自の data 属性（カスタム属性）を設定する
created: 2015-02-20
---

HTML5 では、`data-*` という形式の名前で、カスタム属性を指定することができます。

以下の例では、`data-message` という独自属性を設定しています。

~~~ html
<div id="sample" data-message="Hello World"></div>
~~~

この属性値は、JavaScript から次のように取得することができます。

~~~ js
var elem = document.getElementById('sample');
alert(elem.dataset.message);
~~~

DOM 要素のプロパティである `dataset` は、HTML5 API として定義されています（dataset IDL 属性）。
HTML5 以前も `getAttribute()` を使用すれば、同様のことを実現できますが、dataset IDL 属性の導入により、より統一された形式で、より簡単にカスタム属性を扱うことができるようになりました。

jQuery を使用すれば、よりシンプル `data()` メソッドを使って取得することができます。

~~~ js
var $elem = $('#sample');
alert($elem.data('message'));
~~~

jQuery の `attr()` メソッドが属性値を一律に文字列データとして返すのに比べ、`data()` メソッドは適切な型で値を返します。
オブジェクトとして取得するには、属性値の中で定義されているオブジェクトのプロパティ名を、ちゃんとダブルクォーテーションで囲む必要があることに注意してください。

#### HTML ファイル

~~~ html
<div id="sample"
  data-my-array='[10, 20, 30]'
  data-my-object='{"aaa":100, "bbb":200}'>
</div>
~~~

#### JavaScript

~~~ js
var $elem = $('#sample');

// カスタム属性値を配列として取得
var arr = $elem.data('myArray');
alert(arr[0]);  //=> 10

// カスタム属性地をオブジェクトとして取得
var obj = $elem.data('myObject');
alert(obj.aaa);  //=> 100
~~~

