# Twitter Desktop App
 
Twitterをデスクトップアプリで、  
ログイン -> ツイート -> DBにツイート内容を記録  
までをボタン1つで行うことのできるアプリです。
 
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

5. ツイートが更新される  
![スクリーンショット 0003-09-06 午後4 56 31](https://user-images.githubusercontent.com/66200485/132181325-f2d232b8-113f-4e17-ad21-0a26bbf039cd.png)

6. Chromが閉じる  

# RDB
![スクリーンショット 0003-09-06 午後5 06 08](https://user-images.githubusercontent.com/66200485/132182523-dedb9e0b-a71c-4813-99cb-0066602acc91.png)  
<br>

データベースの確認
```bash
$ sqlite3 database.db
sqlite3 > SELECT * FROM tweet_data;
```



# Requirement
 
**言語**：Python 3.8.8  
**フレームワーク**：Tkinter 8.6  
**開発環境**：MacOS  
**DB**：SQlite3    

# Installation
 
# Usage
 
## APP
1. このリポジトリをclone
```bash
git clone https://github.com/tomohiko9090/Twitter-Desktop-App.git
```
2. 「Twitter-Desktop-App」のディレクトリに移動
```bash
cd Twitter-Desktop-App
```
4. main.py中にある「アカウント情報」を入力
5. main.pyを実行
```bash
python3 main.py
```

## DB
1. SQlite3に入る
```bash
sqlite3 database.db
```
2. 閲覧したいカテゴリーを全て取得
```bash
sqlite3 > SELECT * FROM tweet_data where ;
```

## Next
1. カテゴリーを選択すると、アプリ上でデータベースの内容が簡単に閲覧できるようにする


# Author
 
* 作成者 Hikotomo!
