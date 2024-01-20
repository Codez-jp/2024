# CRUD app with Flask

## 説明
Flask の Hello world サンプル。

## 前提条件
Pythonの仮想環境

以下はvenvを使った仮想環境の構築例。

1. プロジェクトのルートで以下コマンドを実行
venvディレクトリに仮想環境を構築
```
$ python -m venv .venv
```

2. 仮想環境を有効化
構築先のディレクトリである (.vnev) がプロンプトに表示される
```
$ .venv\Scripts\activate
(.venv) C:\Users\(user_root)\public\2024\src\flask_crud>
```

## インストール手順
プロジェクトのルートで以下コマンドを実行
requirements.txtに記載されたパッケージがインストールされる
```
$ pip install -r requirements.txt
```

## 使用法
1. アプリの起動
デフォルト設定ではポート5000で Flask のWEBサーバーが起動する
```python
$ python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

2. 動作確認
ブラウザで以下にアクセスするとメッセージが表示される
http://localhost:5000/
