---
title: "改行、タブ文字、行末のスペースを表示する (list, listchars)"
date: "2011-04-24"
---

改行、タブ文字、行末スペースを表示するための設定
----

下記のように list モードを設定すると、タブや改行文字、末尾の半角スペースなど、通常は非表示の文字を目に見える記号で表示することができます。

~~~ vim
:set list    " 制御文字を表示
:set nolist  " 制御文字を非表示
~~~

一時的に表示して確認したい場合は、以下のように行範囲を指定して `list` コマンドを実行します。

~~~
:1,$ list
:% list
~~~

デフォルトでは、タブ文字が `^I`、改行が `$` で表示されます。


どのように表示するかの設定
----

それぞれの非表示文字をどのような文字で表示するかは、`listchars` (`lcs`) オプションで設定することができます（規定値は `eol:$` です）。

#### ~/.vimrc

~~~ vim
" 行末を '$'、タブを '>...'、末尾のスペースを '_' で表示
set listchars=eol:$,tab:>.,trail:_
set list
~~~

以下のように表示文字に Unicode を指定することもできます（Damian Conway が紹介していた方法）。

~~~ vim
exec "set listchars=tab:\uBB.,trail:_"
set list
~~~

### 各設定の意味

* `tab:>.` というのは、タブの一文字目を `>` で、二文字目以降を `.` で表示する設定。
* `trail:_` というのは、行末の半角スペースを `_` で表示する設定。
* `set list` で `listchars` の設定を有効にします。

プログラミング言語の Python などでコーディングを行っているときは、タブ文字と通常のスペースを意識して使い分けなければいけないので、このような非表示文字を目に見えるように設定しておくことは重要です。
もちろん通常の文章を記述するときにも、行末の余計なスペースなどを簡単に見つけられるようになるので、この設定は常に有効にしておくことをオススメします。


listchars オプションの詳細
----

どんな非表示文字を表示できるかは、`:help listchars` で参照できます。
下記はヘルプ表示の抜粋です。

> 'list' モードと :list コマンドでの表示に使われる文字を設定する。
> 値は指定文字列のコンマ区切りのリストである。
>
> - eol:文字
>     - 行末の表示に使われる文字。指定されないと、行末には何も表示されない。
> - tab:2文字
>     - タブ文字の表示に使われる文字。1文字目は1回だけ使われる。2文字目はタブが通常占めるだけの空白を埋めるまで繰り返し表示される。"tab:>-" とすると、タブが4文字の設定では ">---" となる。指定されないと、タブは ^I と表示される。
> - space:文字
>     - スペースの表示に使われる文字。指定されないと、スペースは空白のまま。
> - trail:文字
>     - 行末のスペースの表示に使われる文字。指定されないと、行末のスペースは空白のまま。行末のスペースでは "space" の設定を上書きする。
> - extends:文字
>     - 'wrap' がオフで、行が画面の右端よりも伸びているときに、最終列に表示される文字。
> - precedes:文字
>     - 'wrap' がオフで、最前列で表示されている最初の文字より前にテキストが存在するとき {訳注: 上の行の末尾が画面の右端より伸びているとき} に、最前列に表示される文字。
> - conceal:文字
>     - 'conceallevel' が 1 のときに Conceal されたテキストの代わりに表示される文字。
> - nbsp:文字
>     - ノーブレークスペース文字 (0xA0 (10進数では160) や U+202F) の表示に使われる文字。指定されない場合は空白のまま。訳注: 0xA0はLatin1で改行なしスペースを表す。
>
> 文字 ':' と ',' は使えない。'encoding' が "utf-8" のときはUTF-8の文字が使える。
> そうでないときはprintableな文字 {訳注: 文書先頭を参照} だけが使える。
> 全ての文字は幅が1でなければならない。
>
> ~~~
> 例:
>   :set lcs=tab:>-,trail:-
>   :set lcs=tab:>-,eol:<,nbsp:%
>   :set lcs=extends:>,precedes:<
> ~~~
>
> "eol", "extends", "precedes" には強調表示グループ "NonText" が、"nbsp", "space", "tab" , "trail" には "SpecialKey" が適用される。


参考
----

* [全角スペースを表示する](show-double-byte-space.html)

