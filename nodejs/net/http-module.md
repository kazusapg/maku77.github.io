---
title: http 標準モジュールを使用して HTTP 通信を行う
date: "2013-11-04"
---

http モジュールの基本的な使い方
----

下記は、Node.js の標準モジュールである `http` モジュールを使用して HTTP 通信を行う例です。

レスポンスのデータは、分割された `data` イベントとして受信されるので、`data` イベントが呼び出される度に受信したデータを結合していく必要があるようです（短いデータを受信するときは結合しなくても全体を受信できてしまうので気付きにくいですが）。

```javascript
var http = require('http');
var uri = 'http://www.example.com/';

http.get(uri, function(res) {
  console.log('Status: ' + res.statusCode);
  console.log('Headers: ' + JSON.stringify(res.headers));

  res.setEncoding('utf8');
  var body = '';

  // Receive body chunks
  res.on('data', function (chunk) {
    body += chunk;
  });

  // Finish receiving a body
  res.on('end', function() {
    console.log(body);
  });
});
```

http モジュールでリクエスト時の HTTP ヘッダを指定する場合
----

HTTP リクエストの内容をより詳細に設定したい場合は、`http.get()` の第一引数に URI ではなく、オプションオブジェクトを指定します。
下記の例では、HTTP GET 時のリクエストヘッダとして、`user-agent` などを設定しています。

```javascript
var http = require('http');

var options = {
  hostname: 'eow.alc.co.jp',
  port: 80,
  path: '/search?q=intimidating',
  headers: {
    'user-agent': 'Mozilla/5.0'
  }
};

http.get(options, function(res) {
  console.log('Status: ' + res.statusCode);
  console.log('Headers: ' + JSON.stringify(res.headers));

  res.setEncoding('utf8');
  var body = '';

  // Receive body chunks
  res.on('data', function (chunk) {
    body += chunk;
  });

  // Finish receiving a body
  res.on('end', function() {
    console.log(body);
  });
});
```

