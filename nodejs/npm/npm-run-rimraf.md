---
title: "npm run のスクリプトの中でディレクトリの削除を行う (rimraf)"
date: "2019-10-07"
---

なぜ rimraf が必要か？
----

TypeScript などのトランスパイラを使って Node.js アプリを開発していると、ビルド結果を格納するディレクトリを削除する `clean` コマンド（NPM スクリプト）を定義したくなります。

#### package.json

```json
{
  "scripts": {
    "clean": "rm -rf build"
  }
}
```

これはこれで間違いではないのですが、Linux の `rm` コマンドを使用しているので、OS 依存の `package.json` になってしまいます。

そこで、OS に依存しない `rm -rf` コマンドを実現するのが **`rimraf`** という NPM パッケージです。
`rimraf` は NPM の作者である Isaac 氏が作成しており、安心して使用できます。
`rimraf` という名前は Linux コマンドの `rm -rf` の発音が由来だと言われています。


rimraf の使い方
----

### rimraf のインストール

`rimraf` コマンドは NPM パッケージとして提供されているので、下記のように簡単にインストールすることができます。

```
$ npm install --save-dev rimraf
```

`--save-dev` オプションを付けて、`package.json` の `devDependencies` エントリに追加するようにしましょう。

### rimraf でディレクトリを削除する

下記の `package.json` では、`build` ディレクトリをごっそり削除する `clean` スクリプトを定義しています。

```json
{
  "scripts": {
    "clean": "rimraf build"
  }
}
```

あとは、下記のように `clean` スクリプトを起動するだけで、`build` ディレクトリを削除することができます。
`build` ディレクトリが存在しない場合は何も起こりません。

```
$ npm run clean
```

