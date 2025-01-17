---
title: "行列／ベクトルを結合する"
date: "2017-03-24"
---

下記のような２行３列の行列が２つあるとします。

~~~ matlab
>> A = [1 2 3; 4 5 6]
A =

   1   2   3
   4   5   6

>> B = [11 12 13; 14 15 16]
B =

   11   12   13
   14   15   16
~~~

これらの行列を横方向、あるいは縦方向に繋げて新しい行列を作成することができます。

### 横方向に結合

~~~ matlab
>> C = [A B]
C =

    1    2    3   11   12   13
    4    5    6   14   15   16
~~~

### 縦方向に結合

~~~ matlab
>> D = [A; B]
D =

    1    2    3
    4    5    6
   11   12   13
   14   15   16
~~~

横方向に結合する場合は行のサイズ、縦方向に結合する場合は列のサイズがそれぞれ等しくなっている必要があります（上記の場合は、行列 A と行列 B は形状が同じなので、どちらの方向にも結合できています）。

次のように、直接ベクトルデータを追加するように記述することもできます。

~~~ matlab
>> C = [A; [7 8 9]]
C =

   1   2   3
   4   5   6
   7   8   9

>> D = [A [7; 8]]
D =

   1   2   3   7
   4   5   6   8
~~~

