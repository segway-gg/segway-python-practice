####----ファイル名を一括で変更するscript----####
import os

folder = "C:/Users/YourName/Desktop/test_folder" # 変更したいフォルダのパスを指定

for i, filename in enumerate(os.listdir(folder), start=1): # フォルダ内のファイルを順番に取得
    old_path = os.path.join(folder, filename) # 変更前のファイルパス
    new_path = os.path.join(folder, f"file_{i}.txt") # 変更後のファイルパス
    os.rename(old_path, new_path) # ファイル名を変更

print("リネーム完了！")



####----日付入りのファイルを自動生成するscript----####
import pandas as pd

df = pd.read_csv("sales.csv") # sales.csvを読み込む
print("売上合計:", df["amount"].sum()) # amount列の合計を表示
print("平均単価:", df["amount"].mean()) # amount列の平均を表示



####----日付入りのファイルを自動生成するscript----####
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d") # 今日の日付を取得
filename = f"report_{today}.txt" # ファイル名を作成

with open(filename, "w", encoding="utf-8") as f: # ファイルを作成して開く
    f.write("本日のレポート\n") # ファイルに内容を書き込む

print(f"{filename} を作成しました") # 作成完了メッセージを表示
