# Flask関連
from flask import Flask
from flask import render_template


# Flask のインスタンスを作成
app = Flask(__name__)


@app.route('/')
def greeting():
    # ユーザーの新規作成画面を表示
    return render_template('hello.html', title="Hello World", message="World")


# __main__ というのは、Python が実行された時のトップレベルのスクリプトのこと。
# ファイルが直接実行された場合、処理が実行される。
if __name__ == '__main__':
    # Flask のサーバーを起動
    # デバッグモードを有効にしているので、ソースコードを変更するとホットリロードされる。
    app.run(debug=True)
