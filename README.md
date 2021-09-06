# Twitter Desktop App
 
「Twitter Desktop App」は、 Twitterをデスクトップアプリで ログイン -> ツイート -> DBにツイート内容を記録 までボタン1つで行えるアプリです。
 
# DEMO
例)カテゴリーを「Python」にし、Tweetする場合 
<br>

1. main.pyを実行  
![スクリーンショット 0003-09-06 午後4 38 01](https://user-images.githubusercontent.com/66200485/132179855-c7124c9f-30b1-4cf3-aa57-13876b3e0d40.png)
<br>

2. カテゴリーを選択し、ツイートしたい内容を記入し、「Tweetボタン」をクリック  
![スクリーンショット 0003-09-06 午後4 39 00](https://user-images.githubusercontent.com/66200485/132179983-9f97a3a7-1ce6-4f78-b09d-6803de07aa69.png)
<br>

3. Chromが開き、Twitterがログインされる  
![スクリーンショット 0003-09-06 午後4 40 12](https://user-images.githubusercontent.com/66200485/132180132-f8271a0d-6658-410d-b381-f345d0a2e644.png)
<br>

4. ツイート内容が自動で入力、ツイートボタンが押される  
![スクリーンショット 0003-09-06 午後4 55 56](https://user-images.githubusercontent.com/66200485/132181278-2c9f24cd-a4b9-477f-a546-6c8a0e442068.png)

5. ツイートが更新  
![スクリーンショット 0003-09-06 午後4 56 31](https://user-images.githubusercontent.com/66200485/132181325-f2d232b8-113f-4e17-ad21-0a26bbf039cd.png)

6. Chromが閉じる  

# Features 
 
## Function
1. **ユーザー関連API**  
    1. **ユーザー情報作成API(POST)**  
http://127.0.0.1:8080/user/create  
ユーザ情報を作成します。  
ユーザの名前情報をリクエストで受け取り、ユーザIDと認証用のトークンを生成しデータベースへ保存します。  
    1. **ユーザー情報取得API(GET)**  
http://127.0.0.1:8080/user/get  
ユーザ情報を取得します。  
ユーザの認証と特定の処理はリクエストヘッダのtokenを読み取ってデータベースに照会をします。  
    1. **ユーザー情報更新API(PUT)**  
http://127.0.0.1:8080/user/update  
ユーザ情報の更新をします。  
<br>

2. **ガチャ実行API(POST)**    
http://127.0.0.1:8080/gacha/draw  
ガチャを引いてキャラクターを取得します。  
獲得したキャラクターはユーザ所持キャラクターテーブルへ保存します。  
同じ種類のキャラクターでもユーザは複数所持することができます。  
<br>

3. **ユーザー所持キャラクター一覧取得API(GET)**  
http://127.0.0.1:8080/character/list  
ユーザが所持しているキャラクター一覧情報を取得します。

## RDB
![スクリーンショット 0003-09-06 午後5 06 08](https://user-images.githubusercontent.com/66200485/132182523-dedb9e0b-a71c-4813-99cb-0066602acc91.png)


# Directory Structure
![スクリーンショット 0003-08-29 午後1 29 59](https://user-images.githubusercontent.com/66200485/131238485-d64d0ade-8c53-4f68-a633-5b2fcd94058c.png)

## Model-View-Controller
- M : model層  
DBへアクセスしたり、構造体を作成します。  
- V : view = handler層  
tokenからユーザー情報を読み取ったり、paramからIDを取得したりするなど、クライアントのリクエストとレスポンスを行います。　　
- C : controller層  
tokenを生成したり、確率に応じてキャラを引いたりするなど、ビジネスロジックを組み立てます。  

# Requirement
 
**言語**：Golang 1.16.3  
**フレームワーク**：echo v3.3.10  
**開発環境**：MacOS  
**DB**：MySQL  
**ライブラリ**：  
"github.com/go-sql-driver/mysql"  
"github.com/labstack/echo"  

# Installation

Requirementで列挙したライブラリのインストール方法
 
```bash
go get github.com/go-sqlt-driver/mysql
go get github.com/labstack/echo
```
 
# Usage
 
1. このリポジトリをclone
2. TurtleGachaAPI_MVCmodelのディレクトリに移動
3. main.goを実行
4. HeaderやBodyにKeyとValueを入れてリクエスト

```bash
git clone https://github.com/tomohiko9090/CA_Tech_Dojo.git
cd CA-Tech-Dojo
go run main.go
```
 
# Memo

 綺麗なコーディングを行う上で教わったアドバイスをメモしていきます。
 
## Golang(API)
- 基本的に１単語でファイル名を付けること
- ファイルの１文字目に大文字は使わないこと
- handlerでmodelをよむの×(処理の流れ hendler -> controller -> model　とし、hendlerからmodelに跨がないようにする)
- InsertUser, CreateUserのようにわかりやすい関数名にする
- 「panic」にするとサーバーが落ちてしまうため、エラーハンドリングを行う
- Golandの設定でwatchのgo fmt とgo imports で自動でリフォーマットできるようにする
- 頭文字が大文字のものはPublicとなり、外部packageから参照が可能になる。また、小文字のものはPrivateとなり、外部packageから参照が不可能になる。
- modelでグローバル変数を使いますのはアンチパターン
- Goではスネークケースではなく、キャメルケースを使う
- エラー時、ステータスコードは重要であるため必ず行う
- エラーログはfmt出力でなくlog出力を使用すること(logならファイル保存可能)
- 配列を使用したfor文では、forrを使用すること

## MySQL(DB)
- APIでは一度発行したDBコネクションを使い倒す(毎回接続するのはアンチパターン)
- idなどで,通し番号を付けたい時は、「AUTO_INCREMENT」を使用する。
- UserテーブルとCharacterテーブルの中間テーブルはUserCharacterテーブルという名称になる。

## GitHub
- マスターブランチ(pullリク)は、コメントアウトは少なくし、第三者がコードをみる時に必要なもののみにする。コメントアウトがたくさん入ったものはデベロップブランチへ。

# KeyWords
マッピング : 関連付けを行うこと  
キャスティング : データ型を別の型に変換すること  
リファクター : 内部構造は変えながらもアウトプットは同じにすること  
アッパーキャメルケース : 1文字目大文字  
ローワーキャメル : 1文字目小文字  
 
# Author
 
* 作成者 Hikotomo!
