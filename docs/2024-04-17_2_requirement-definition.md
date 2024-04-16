# ソフトウェア開発手法 5

## 前回のおさらい
前回は、各工程と対になるテストの作成方法について学んだ。
今回は、日報システムを例に、要件定義の工程を実際に手を動かしながら学んでいく。

## 日報システムとは
要件定義は、システムの目的や機能、制約条件などを明確にする工程である。
日報システムは、一般的には、社員が日々の業務内容を記録するためのシステムである。
主な機能としては、日報の作成、編集、削除、検索などがあり、複数部署で利用することを想定する場合、ログイン機能やアクセス権限の設定なども必要になる。

## 要件定義の手順
要件定義の方法は複数あるが、今回はユーザー観点より操作に主眼を置いて、画面遷移図を作成する方法を学ぶ。

### 画面遷移図
画面遷移図は、システム内の画面間の遷移を示す図であり、システムの機能や操作を理解するために有効な手法である。
最初は、画面レイアウトやデザインは考慮せず、ユーザーがどの画面からどの画面に遷移するかに着目する。
また、遷移する際の条件や制約も考慮する。

ヒント:
最低限必要な画面は以下が考えられる
- 日報作成画面
- 日報編集画面
- 日報検索画面
- 日報詳細画面
また、部署毎に違う処理を行う場合、認証関連、部署毎の画面を必要に応じて用意する。

### 画面レイアウト
画面遷移図の作成が終わったら、次は画面レイアウトを考える。
画面レイアウトは、画面のデザインや配置を示す図であり、ユーザーが操作しやすいように設計する。
最初は、ボタンやテキストボックスの要不要など、基本的な機能を満たすかに着目する。
最後に、画面のデザインや色使い、フォントサイズなどを考慮する。

## 次回予告
次回は **基本設計** を実際に手を動かしながら検討していく。