---
title: "オーディオファイル (mp3) を再生する"
date: "2013-07-21"
---

Audio クラスを使用して、mp3 などの音声ファイルを再生することができます。
下記の例では、画面上に表示された Play ボタンを押したときに、mp3 ファイルを再生します。

~~~ html
<button onclick="playSound()">Play</button>

<script>
function playSound() {
  var audio = new Audio('./audio/001.mp3');
  audio.play();
}
</script>
~~~

