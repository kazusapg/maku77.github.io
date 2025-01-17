---
title: "Rust でモジュールを定義する (mod)"
url: "p/gxj4n7q/"
date: "2023-03-05"
tags: ["Rust"]
---

規模の大きい Rust プログラムを作る場合、__モジュール__ の仕組みを使ってコードを階層化すると見通しがよくなります。
Rust でモジュールを定義するときは、__`mod`__ キーワードを使用します。
1 つの `.rs` ファイルの中にインライン形式でモジュールを定義することも、別ファイルに分けてモジュールを定義することもできます。


クレートとモジュール
----

すべての Rust プログラムはクレート (crate) であり、__バイナリクレート__ か __ライブラリクレート__ のどちらかです。
クレートは、Rust におけるコンパイルの単位です。

- バイナリクレート ... 1 つの実行ファイルを作り上げるもの。
- ライブラリクレート ... 1 つのライブラリを作り上げるもの。

コンパイルはクレート単位で行われますが、コードレベルの実装では、__モジュール__ という論理的な単位で分割／階層化できるようになっています。
クレートは 1 つ以上のモジュールで構成され、必ず 1 つの __ルートモジュール（クレートルート）__ を持っています。
ルートモジュールのファイル名は決まっていて、バイナリクレートの場合は __`src/main.rs`__ で、ライブラリクレートの場合は __`src/lib.rs`__ です。
ルートモジュールはサブモジュールを含むことができ、さらに、サブモジュールも同様にサブモジュールを含むことができます。

{{< code title="クレートの論理的構造" >}}
ルートモジュール (main.rs あるいは lib.rs)
  +-- サブモジュール
  |     +-- サブサブモジュール
  |     +-- ...
  +-- サブモジュール
        +-- サブサブモジュール
        +-- ...
{{< /code >}}

上記のように、クレート内のモジュールはルートモジュールを起点とするツリー構造になるため、`mod` キーワードを使ってモジュールを定義するとき、それは必ず何らかの親モジュールのサブモジュールということになります。


モジュールの作り方
----

### インラインモジュール

`mod` ブロックを使ってサブモジュールを定義することができます。
サブモジュールの実装をブロック内に直接記述するので、__インラインモジュール__ と呼ばれます。
次の例では、`calc` モジュールを定義して、その中に `add` 関数を定義しています。

{{< code lang="rust" title="src/main.rs" >}}
// calc モジュールを定義する
mod calc {
    pub fn add(a: i32, b: i32) -> i32 {
        a + b
    }
}

fn main() {
    // calc モジュール内の add 関数を呼び出す
    println!("{}", calc::add(1, 2));
}
{{< /code >}}

モジュール内で定義した関数は、デフォルトでモジュール内からのみ参照可能 (private) になっているため、別モジュールから `add` 関数を呼び出せるようにするには __`pub`__ キーワードを付けて公開設定しておく必要があります（`pub` の詳細は後述）。
親モジュール（ここではルートモジュール）から `calc` モジュールの `add` 関数にアクセスするには、__`calc::add`__ というパスを使用します。

### ファイルモジュール

サブモジュールを別ファイルとして実装することもできます。
というより、大きなプロジェクトを管理する場合、こちらのファイルを使ったサブモジュール化が主な使い方になると思います。

例えば、ルートモジュール (`main.rs`) から呼び出すことのできる `calc` サブモジュールを作るには、`main.rs` と同じディレクトリに、__`calc.rs`__ あるいは __`calc/mod.rs`__ を配置します。
つまり、ディレクトリ構成は次のようになります。

{{< code title="calc モジュールの配置方法 (1) 2018 edition 以降" hl_lines="3" >}}
src/
  +-- main.rs
  +-- calc.rs
{{< /code >}}

{{< code title="calc モジュールの配置方法 (2) 2015 edition 以降" hl_lines="3 4" >}}
src/
  +-- main.rs
  +-- calc/
        +-- mod.rs
{{< /code >}}

別ファイルに分離した `calc` モジュールのコードは次のようになります。
先ほど `mod calc` ブロックの中に記述したコードと同じ内容です。

{{< code lang="rust" title="src/calc.rs" >}}
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
{{< /code >}}

これをルートモジュールから利用するには、次のように __`mod calc;`__ というモジュール宣言を行うことで、`src/calc.rs`（あるいは `src/calc/mod.rs`）の内容を読み込むようコンパイラに指示します。
あとは、先ほどの例と同様、`calc::add` という形でモジュール内の関数を呼び出せます。

{{< code lang="rust" title="src/main.rs" >}}
mod calc;  // コンパイラに calc.rs（あるいは calc/mod.rs）が存在することを知らせる

fn main() {
    println!("{}", calc::add(1, 2));
}
{{< /code >}}


サブサブモジュール
----

サブモジュール内でさらに `mod` キーワードを使えば、ネストする形でサブモジュールを定義することができます（以下、サブサブモジュール）。
ここでは例として、__`sub`__ という名前のサブモジュールと、__`subsub`__ という名前のサブサブモジュールを作ることにします。
サブサブモジュールは、サブモジュールと同じ名前のディレクトリ名 (`sub`) に `.rs` ファイルを配置することで作成できます。

{{< code title="サブサブモジュールの配置" hl_lines="3-5" >}}
src/
  +-- main.rs
  +-- sub.rs （サブモジュール）
  +-- sub/
       +-- subsub.rs （サブサブモジュール）
{{< /code >}}

あるいは、`mod.rs` を使う場合は次のような配置になります。
`src` ディレクトリの一階層目をスッキリさせたいときは、こちらの配置の方がよいですね。

{{< code hl_lines="3-5" >}}
src/
  +-- main.rs
  +-- sub/
       +-- mod.rs （サブモジュール）
       +-- subsub.rs （サブサブモジュール）
{{< /code >}}

以下、それぞれの `.rs` ファイルの実装例です。
`pub` キーワードで公開設定しなければいけないのは、サブサブモジュールでも同様です（ここでは文字列定数 `MY_NAME` を公開設定しています）。

{{< code lang="rust" title="main.rs（ルートモジュール）" >}}
mod sub;  // sub.rs の存在を知らせる

fn main() {
    sub::hello();  //=> "Hello, Maku"
}
{{< /code >}}

{{< code lang="rust" title="sub.rs（サブモジュール）" >}}
mod subsub;  // sub/subsub.rs の存在を知らせる

pub fn hello() {
    println!("Hello, {}", subsub::MY_NAME);
}
{{< /code >}}

{{< code lang="rust" title="sub/subsub.rs（サブサブモジュール）" >}}
pub const MY_NAME: &str = "Maku";
{{< /code >}}

デフォルトでは、サブモジュールには、その親モジュールからしかアクセスできないようになっています。
上記の例で言うと、ルートモジュール (`main.rs`) からの `sub` モジュールの参照や、`sub` モジュールからの `subsub` モジュールの参照は可能ですが、ルートモジュールから直接 `subsub` モジュールを参照することはできません。
`sub` モジュールの外から `subsub` モジュールにアクセスできるようにするには、次のように __`pub mod`__ を使ってモジュールを公開設定します。

{{< code lang="rust" title="sub.rs" >}}
pub mod subsub;
{{< /code >}}

ここまで、`pub` キーワードを付けて公開設定してきたのは、モジュール内のメンバー（関数や定数）でしたが、ネストされたモジュールの公開設定も同様の仕組みで行えるということですね。
下記のサンプルコードでは、ルートモジュール (`main.rs`) から、サブサブモジュールに直接アクセスしています（`sub::subsub` という階層化されたパスを使用します）。

{{< code lang="rust" title="main.rs（ルートモジュール）" hl_lines="6 7" >}}
mod sub;

fn main() {
    println!("VALUE_1 = {}", sub::VALUE_1);  //=> 100
    println!("VALUE_2 = {}", sub::VALUE_2);  //=> 200
    println!("VALUE_3 = {}", sub::subsub::VALUE_3);  //=> 300
    println!("VALUE_4 = {}", sub::subsub::VALUE_4);  //=> 400
}
{{< /code >}}

{{< code lang="rust" title="sub.rs（サブモジュール）" hl_lines="1" >}}
pub mod subsub;  // subsub モジュールを公開設定
pub const VALUE_1: i32 = 100;
pub const VALUE_2: i32 = 200;
{{< /code >}}

{{< code lang="rust" title="sub/subsub.rs（サブサブモジュール）" >}}
pub const VALUE_3: i32 = 300;
pub const VALUE_4: i32 = 400;
{{< /code >}}

ちなみに、`sub::subsub::VALUE_3` と絶対パス指定している部分は、__`use`__ を使って次のように省略記述 (`subsub::VALUE_3`) できるようになります。

{{< code lang="rust" title="main.rs" hl_lines="2 6" >}}
mod sub;
use sub::subsub;

fn main() {
    // ...
    println!("VALUE_3 = {}", subsub::VALUE_3);
}
{{< /code >}}


公開範囲を制限する
----

ここまでの例では、シンプルな `pub` 指定による公開設定をしていましたが、これは、正確には __外部のクレートにまで公開する__ という意味になります。
外部クレートに公開するといっても、実際には、サブモジュールを `pub` 修飾しない限り、サブモジュール内のメンバーには外からはアクセスできないので、それだけで情報がダダ漏れになるということはありません。
とはいえ、公開範囲はできるだけ絞った方がよく、次のような追加のパス指定で、細かく公開範囲を制御できるようになっています。

| 指定方法 | 意味 |
| ---- | ---- |
| `pub` | 外部のクレートにまで公開 |
| `pub(crate)` | カレントクレートに公開 |
| `pub(super)` | 親モジュールに公開 |
| `pub(super::super)` | 親モジュールの親モジュールに公開 |
| `pub(in crate::my_mod)` | 指定したパスのモジュールに公開（上位のモジュールのみを指定可能） |
| （指定なし） | プライベート（モジュール内でのみ参照可能） |
| `pub(self)` | 同上（モジュール内でのみ参照可能） |

上の指定方法の中でも使っていますが、モジュールパスは次のようなプレフィックスを組み合わせて指定することができます。

- `self::` ... 自分自身のモジュールからの相対パス
- `super::` ... 親モジュールからの相対パス
- `crate::` ... クレートルートからの絶対パス

クレート内でのみ使用する要素には、__`pub(crate)`__ 以上の公開範囲（つまり `pub`）を設定する必要はありません。
一般的に、モジュールの依存関係はツリー構造に従ったシンプルな構成になっていると保守しやすいので、まずは __`pub(super)`__ で公開設定できないかを考えてみるとよいです。

