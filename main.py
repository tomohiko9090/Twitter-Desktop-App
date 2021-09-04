# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

# 空のデータベースを作成して接続する
dbname = "database.db"
c = sqlite3.connect(dbname)
c.execute("PRAGMA foreign_keys = 1")

# 既にデータベースが登録されている場合は、ddlの発行でエラーが出るのでexceptブロックで回避する
try:
    # itemテーブルの定義
    ddl = """
    CREATE TABLE item
    (
       item_code INTEGER PRIMARY KEY 
       AUTOINCREMENT,
       item_name TEXT NOT NULL UNIQUE
    )
     """
    # SQLの発行
    c.execute(ddl)
    # acc_dataテーブルの定義    
    ddl = """
    CREATE TABLE acc_data
    ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        acc_date DATE NOT NULL,
        item_code INTEGER NOT NULL,
        amount INTEGER,
        FOREIGN KEY(item_code) REFERENCES item(item_code)
    )
    """
    # itemテーブルへリファレンスデータの登録
    c.execute(ddl)
    c.execute("INSERT INTO item VALUES(1,'食費')")
    c.execute("INSERT INTO item VALUES(2,'住宅費')")
    c.execute("INSERT INTO item VALUES(3,'光熱費')")
    c.execute("COMMIT")
except:
    pass
# -------------------------------
# 内訳テーブル(item)にあるitem_nameのタプルを作成する
def createitemname():
    # データベースの接続
    c = sqlite3.connect("database.db")
    # 空の「リスト型」を定義
    li = []
    # SELECT文を発行し、item_nameを取得し、for文で回す
    for r in c.execute("SELECT item_name FROM item"):
        # item_nameをリストに追加する
        li.append(r)
    # リスト型のliをタプル型に変換して、ファンクションに戻す
    return tuple(li)
# ------------------------------
# 登録ボタンがクリックされた時にデータをDBに登録するコールバック関数
def create_sql(item_name):

    # データベースに接続
    c = sqlite3.connect("database.db")
    # item_nameをWHERE句に渡してitem_codeを取得する
    item_code = c.execute("""
         SELECT item_code FROM item
         WHERE item_name = '{}'
         """.format(item_name))
    item_code = item_code.fetchone()[0]
    # 日付の読み取り
    acc_data = entry1.get()
    # 金額の読み取り
    amount = entry3.get()

    # SQLを発行してDBへ登録
    try:
        c.execute("""
        INSERT INTO 
        acc_data(acc_date,item_code,amount)
        VALUES('{}',{},{});
        """.format(acc_data,item_code,amount))
        c.execute("COMMIT;")
        print("1件登録しました")
    # ドメインエラーなどにより登録できなかった場合のエラー処理
    except:
        print("エラーにより登録できませんでした")

# rootフレームの設定
root = tk.Tk()
root.title("爆速ツイートアプリ")
root.geometry("300x280")

# メニューの設定
frame = tk.Frame(root,bd=2,relief="ridge")
frame.pack(fill="x")
button1 = tk.Button(frame,text="入力")
button1.pack(side="left")
button2 = tk.Button(frame,text="表示")
button2.pack(side="left")
button3 = tk.Button(frame,text="終了")
button3.pack(side="right")

# 入力画面ラベルの設定
label1 = tk.Label(root,text="【入力画面】",font=("",16),height=2)
label1.pack(fill="x")

# 日付のラベルとエントリーの設定
frame1 = tk.Frame(root,pady=10)
frame1.pack()
label2 = tk.Label(frame1,font=("",14),text="日付")
label2.pack(side="left")
entry1 = tk.Entry(frame1,font=("",14),justify="center",width=15)
entry1.pack(side="left")

# 内訳のラベルとエントリーの設定
frame2 = tk.Frame(root,pady=10)
frame2.pack()
label3 = tk.Label(frame2,font=("",14),text="内訳")
label3.pack(side="left")
# 内訳コンボボックスの作成
combo = ttk.Combobox(frame2, state='readonly',font=("",14),width=13)
combo["values"] = createitemname()
combo.current(0)
combo.pack()

# 金額のラベルとエントリーの設定
frame3 = tk.Frame(root,pady=10)
frame3.pack()
label4 = tk.Label(frame3,font=("",14),text="金額")
label4.pack(side="left")
entry3 = tk.Entry(frame3,font=("",14),justify="center",width=15)
entry3.pack(side="left")

# 登録ボタンの設定
button4 = tk.Button(root,text="ついーと",
                    font=("",16),
                    width=10,bg="gray",
                    command=lambda:create_sql(combo.get()))
button4.pack()

# メインループ
root.mainloop()