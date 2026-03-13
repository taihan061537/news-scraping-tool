# Yahoo News Scraper

## Overview

Pythonを使用してYahooニュースのタイトルとURLを取得し、CSVファイルに保存するスクレイピングツールです。
ニュースサイトからデータを取得し、データをCSV形式で保存することで簡単に分析できる形にします。

---

## Tools

* Python
* requests
* BeautifulSoup
* csv

---

## Features

* WebページのHTML取得
* 日本語文字コードの調整（文字化け対策）
* ニュースタイトルとURLの取得
* CSVファイルへの保存
* 取得したニュースの表示

---

## Output

プログラムを実行すると `news.csv` が生成されます。

| タイトル     | URL   |
| -------- | ----- |
| ニュースタイトル | 記事リンク |

---

## How It Works

1. YahooニュースのHTMLを取得
2. BeautifulSoupでHTMLを解析
3. aタグからタイトルとURLを取得
4. Yahooニュースのリンクのみ抽出
5. 上位20件をCSVに保存

---

## Example Output

```
タイトル,URL
ニュースタイトル1,https://news.yahoo.co.jp/...
ニュースタイトル2,https://news.yahoo.co.jp/...
ニュースタイトル3,https://news.yahoo.co.jp/...
```

---

## File Structure

```
news-scraper
 ├ news_scraper.py
 ├ news.csv
 └ README.md
```
