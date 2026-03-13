import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.yahoo.co.jp/"

response = requests.get(url)#urlのhtmlタグを取得
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")#"html.parser"は解析方法

news_list = soup.find_all("a")


data = []

for news in news_list:
    title = news.text.strip()
    link = news.get("href")

    if title != "" and link is not None :
        data.append([title, link])
        print(title, link)

data = data[:20]

with open("news.csv", "w", newline="", encoding="utf-8-sig") as file:#
    writer = csv.writer(file)
    writer.writerow(["タイトル", "URL"])#これはタイトル、urlというカラムを取得している
    writer.writerows(data)#データを集めて最終的にファイルに書いている

print("news.csv を作成しました")


print(len(data), "件取得しました")