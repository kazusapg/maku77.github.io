---
title: "Date オブジェクト同士の差分を取る"
date: "2018-04-04"
---

Date オブジェクト同士の差分を取って、その日数差や時間差を調べたい時などは、`Date#getTime()` で得られるミリ秒単位のタイムスタンプをもとに計算します。
例えば、2つの Date オブジェクトの日数差を調べたいのであれば、まず、ミリ秒単位の差分を求め、それを1日あたりのミリ秒 (86400000 = 24 * 60 * 60 * 1000) で割れば求められます。

下記の関数 `calcDayOffset` は、与えられた2つの Date オブジェクトの日数差を計算します。
小数点以下は切り上げ (`Math.ceil`) しています。

~~~
function calcDayOffset(date1, date2) {
  // 1日あたりの秒数
  var MILLISECONDS_IN_A_DAY = 24 * 60 * 60 * 1000;
  var diffMillis = date2.getTime() - date1.getTime();
  // 小数点以下は切り上げ
  return Math.ceil(diffMillis / MILLISECONDS_IN_A_DAY)
}
~~~

2018年1月1日から2018年2月1日まで何日あるかを計算するには次のようにします。

~~~
var d1 = new Date(2018, 0, 1);  // 2018年1月1日
var d2 = new Date(2018, 1, 1);  // 2018年2月1日
console.log(calcDayOffset(d1, d2));  //=> 31
~~~

