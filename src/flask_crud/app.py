# Python標準
import os

# Flask関連
from flask import Flask, request, render_template, redirect, jsonify

# SQLAlchemy関連
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
SQLALCHEMY_DB_NAME = 'sqlite.db'
# データベースを作成するための基底クラスとして Base クラスを SQLAlchemy
# の DeclarativeBase クラスを継承する形で定義する。
class Base(DeclarativeBase):
    pass


# SQLAlchemy のインスタンスを作成
db = SQLAlchemy(model_class=Base)
# Flask のインスタンスを作成
app = Flask(__name__)

# SQLAlchemy で使うデータベースの URI を設定
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{SQLALCHEMY_DB_NAME}'
# db に app を紐づける
db.init_app(app)


# User という名前のテーブルを作成
class User(db.Model):
    # id を int 型の主キーとして定義
    id: Mapped[int] = mapped_column(primary_key=True)
    # name を str 型のカラムとして定義
    name: Mapped[str] = mapped_column(unique=True)

    # 辞書型でデータを返す
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# 実体がない場合、データベースを作成する。
db_path = os.path.join(
    os.path.dirname(__file__),  # このファイルのディレクトリ
    f"instance\\{SQLALCHEMY_DB_NAME}")  # データベースの実体の格納先

if not os.path.exists(db_path):
    # context というのは、Flask がリクエストを処理するために必要な情報を
    # 一時的に保持する場所のこと。
    # ここでは、Flask インスタンスである app に紐づいた情報を使う
    with app.app_context():
        # データベースのテーブルを作成する。
        db.create_all()
        print('データベースを作成しました。')


# Create
@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        # フォームに入力された内容を取得
        name = request.form['name']
        # User クラスのインスタンスを作成
        user = User(name=name)
        # データ処理を開始 ※この時点ではデータベースには未反映
        db.session.add(user)
        # データベースに反映
        db.session.commit()
        # 一覧画面を表示
        return redirect('/users')
    # GET
    # ユーザーの新規作成画面を表示
    return render_template('new.html', title="新規追加", user=None)


# Read all
@app.route('/users', methods=['GET'])
def index_users():
    # 全ユーザーを取得
    users = User.query.all()
    # 一覧画面を表示
    return render_template('index.html', users=users)
    # JSON形式で返す場合
#    return jsonify([user.as_dict() for user in users])


# Read one by id
@app.route('/user/<id>', methods=['GET'])
def detail_user(id):
    # id で指定されたユーザーを取得
    user = User.query.get(id)
    return render_template('detail.html', user=user)


# Update
# 処理はほぼ Create と同じ
@app.route('/user/<id>/update', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get(id)
    if request.method == 'POST':
        name = request.form['name']
        user.name = name
        db.session.commit()
        return redirect('/users')
    # GET
    return render_template('new.html', title="更新", user=user)


# Delete
@app.route('/user/<id>/delete', methods=['DELETE'])
def delete_user(id):
    # id で指定されたユーザーを取得
    user = User.query.get(id)
    # データベースの削除処理を開始 ※この時点ではデータベースには未反映
    db.session.delete(user)
    # データベースに反映
    db.session.commit()
    # 一覧画面を表示
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)