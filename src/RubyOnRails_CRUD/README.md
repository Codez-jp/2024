# Ruby on Rails CRUD app

## 1. Hello world 同様 Piza Cloud を利用する。

https://paiza.cloud

## 2. プロジェクトを作成する
- myCRUDApp フォルダ以下にプロジェクトを作成する
このコマンド一発でプロジェクトに必須のファイルやディレクトリが作成される
```bash
$ rails new myCRUDApp
```

## 3. プロジェクトのディレクトリに移動する
```bash
$ cd myCRUDApp
```

## 4. rails generate コマンドで scaffold（足場）を作成する
- Todo モデルを作成する
- string 型の title のカラムを作成する
- text 型の content のカラムを作成する
```bash 
$ rails generate scaffold Todo title:string content:text
```
## 5. データベースを作成する
デフォルトのデータベースは SQLite3 であり、db フォルダ以下に development.sqlite3 などのファイルが作成される。
```bash
$ rake db:migrate
```

## 6. サーバーを起動する
```bash
$ rails server
```

## 7. ブラウザでアクセスする
- ブラウザで http://localhost:3000/todos にアクセスする
- Todo モデルの CRUD 操作ができる画面が表示されれば成功