import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

import time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

c = sqlite3.connect("database.db")
c.execute("PRAGMA foreign_keys = 1")

# 既にデータテーブル作成されている場合は、exceptブロックで回避
try:
    ddl = """
    CREATE TABLE tweet_category
    (
        category_code INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL UNIQUE
    )
        """
    c.execute(ddl)

    ddl = """
    CREATE TABLE tweet_data
    ( 
        number INTEGER PRIMARY KEY AUTOINCREMENT,
        category_code INTEGER NOT NULL,
        content barchar NOT NULL,
        FOREIGN KEY(category_code) REFERENCES tweet_category(category_code)
    )
    """
    c.execute(ddl)
    c.execute("INSERT INTO tweet_category VALUES(1,'Python')")
    c.execute("INSERT INTO tweet_category VALUES(2,'Golang')")
    c.execute("INSERT INTO tweet_category VALUES(3,'チーム開発')")
    c.execute("COMMIT")
except:
    pass

# カテゴリーを取得し配置
def select_category_name():
    # データベースの接続
    c = sqlite3.connect("database.db")
    category_l = []
    for r in c.execute("SELECT category_name FROM tweet_category"):
        category_l.append(r)
    return tuple(category_l)

def max_number():
    c = sqlite3.connect("database.db")
    max_number = [r for r in c.execute("select max(number) from tweet_data")][0][0]
    return max_number

# rootフレームの設定
root = tk.Tk()
root.title("爆速Tweetアプリ")
root.geometry("340x300")

# 入力画面ラベルの設定
label1 = tk.Label(root, text="【memo】", font=("", 16), height=2)
label1.pack(fill="x")

haruna = tk.PhotoImage(file="news_oshirase_img_twitter_bird.png")
canvas = tk.Canvas(width=150, height=150)
canvas.place(x=115, y=170)
canvas.create_image(0, 0, image=haruna, anchor=tk.NW)

# カテゴリーのラベルとエントリーの設定
frame1 = tk.Frame(root, pady=10)
frame1.pack()
label2 = tk.Label(frame1, font=("", 14), text="カテゴリー：")
label2.pack(side="left")
# カテゴリーコンボボックスの作成
combo = ttk.Combobox(frame1, state='readonly', font=("", 14), width=10)
combo["values"] = select_category_name()
combo.current(0)
combo.pack()

# 内容のラベルとエントリーの設定
frame2 = tk.Frame(root, pady=10)
frame2.pack()
label3 = tk.Label(frame2, font=("", 14), text="内容：")
label3.pack(side="left")
entry = tk.Entry(frame2, font=("", 14), justify="left", width=30)
entry.pack(side="left")

# アカウント情報
account = 'username'
password = 'password'


# Twitterログイン実行する処理
def login_twitter(driver):
    # ログイン処理
    time.sleep(1)  # 待ち

    # account入力
    element_account = driver.find_element_by_name("session[username_or_email]")
    element_account.send_keys(account)
    time.sleep(0.3)  # 待ち

    # パスワードを入力する
    element_pass = driver.find_element_by_name("session[password]")
    element_pass.send_keys(password)
    time.sleep(0.3)  # 動作止める

    # ログインボタンクリック
    element_login = driver.find_element_by_xpath('//*[@data-testid="LoginForm_Login_Button"]')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element_login.click()
    time.sleep(0.3)  # 待ち


def send_tweet(driver, category_name):
    time.sleep(0.3)  # 待ち
    element_text = driver.find_element_by_class_name("notranslate")
    element_text.click()
    content = entry.get()
    element_text.send_keys("No.{}\n学んだこと：{}\nメモ：{}".format(max_number()+1, category_name, content))#
    tweet_button = driver.find_element_by_xpath('//*[@data-testid="tweetButtonInline"]')
    tweet_button.click()


def twitter_control(category_name):
    # seleniumを起動 
    options = Options()
    driver = webdriver.Chrome(chrome_options=options)

    # ログインページを開く
    driver.get('https://twitter.com/login/')
    login_twitter(driver)

    # ツイートする
    send_tweet(driver, category_name)
    time.sleep(1)

    # seleniumを終了
    driver.close()
    driver.quit()


# Tweetボタンがクリックされた時にデータをDBに登録するコールバック関数
def create_sql(category_name):
    twitter_control(category_name)
    # データベースに接続

    c = sqlite3.connect("database.db")
    category_code = c.execute(
        """SELECT category_code FROM tweet_category WHERE category_name = '{}'""".format(category_name))

    category_code = category_code.fetchone()[0]
    content = entry.get()

    # DBへ登録
    try:
        c.execute(
            """
            INSERT INTO 
            tweet_data(category_code, content)
            VALUES({},"{}");
            """.format(category_code, content))
        c.execute("COMMIT;")
        print("Tweet完了")
    # ドメインエラーなどにより登録できなかった場合のエラ
    except:
        print("error:TweetがDBに保存できませんでした")

button = tk.Button(root, text="Tweet",
                   font=("", 14),
                   width=10,
                   highlightbackground="#00acee",
                   foreground='#00acee',
                   command=lambda: create_sql(combo.get())
                   )
button.pack()

# メインループ
root.mainloop()
