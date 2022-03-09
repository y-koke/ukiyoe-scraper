# ukiyoe-scraper

This tool is to automatically save ukiyoe images from the ARC Ukiyoe Portal database.
You must specify the author name with runtime arguments.
The search target is only the landmark category.

## Requirement

* Python 3.9.7
* Requests 2.27.1
* BeautifulSoup4 4.10.0

## Sample command


`python scraping_by_artist.py 広重`  
`python scraping_by_artist.py 広重 --maxnum 1000 --skip 500 --sleep True`

# 浮世絵スクレイピングツール

ARC浮世絵ポータルデータベースから浮世絵画像を自動保存するツールです。  
実行時引数で作者名を指定する必要があります。  
検索対象は名所絵のみです。

## 必要なライブラリ

* Python 3.9.7
* Requests 2.27.1
* BeautifulSoup4 4.10.0

## サンプルコマンド

`python scraping_by_artist.py 広重`  
`python scraping_by_artist.py 広重 --maxnum 1000 --skip 500 --sleep True`
