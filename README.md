# 目的
紙の本のページの写真を撮るだけで要約・解説してくれます。

# 仕組み
1. GoogleのCloud Vision AIを用いて、画像から文字を読み取る。
2. Java Scriptで次のAPIが処理しやすいように整形する。
3. Open AIのAPIを用いて読み取った文章を要約する。
3. クライアント側に出力する。
