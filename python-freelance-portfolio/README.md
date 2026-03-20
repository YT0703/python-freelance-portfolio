# Python Freelance Portfolio

クラウドソーシング案件を想定したPythonサンプルコードです。  
実務案件を意識し、再利用性・拡張性を重視した構成で作成しています。

---

## 対応可能案件

・CSVデータ処理  
・APIデータ取得  
・Webスクレイピング  
・Pythonコード修正  

---

## Books Scraping Tool（NEW）

Books to Scrape（練習用サイト）から書籍データを取得し、CSVに保存するツールです。

### ■ 機能
- ページネーション対応（複数ページ一括取得）
- 書籍データのスクレイピング
- CSV保存
- 重複データ削除
- エラーハンドリング対応
- ログ出力（実行状況の可視化）
- 実行時間計測

### ■ 取得データ
- タイトル
- 価格（数値型に変換済み）
- 在庫状況
- 評価（★ → 数値化）
- 商品URL

### ■ 実行結果
- 約100件の書籍データを取得（5ページ分）
- 1ページあたり約20件取得
- CSVファイルとして出力

### ■ 技術ポイント
- BeautifulSoupによるHTML解析
- requestsによるデータ取得
- 正規表現によるデータクレンジング
- 文字化け対策（エンコーディング補正）
- 実務を想定したエラーハンドリング実装

### ■ ファイル構成

books_scraping_tool/
├── main.py
├── scraper.py
├── utils.py
├── config.py


---

## CSV Auto Processor

CSVファイルを読み込み、カテゴリーごとの合計を計算するツールです。

### ■ 機能
- CSV読み込み
- データ集計
- 新CSV作成

### ■ ファイル
csv_auto_processor/csv_summary.py

---

## API Data Collector

APIからJSONデータを取得してCSVに保存するツールです。

### ■ 機能
- APIリクエスト
- JSONデータ解析
- CSV保存

### ■ ファイル
api_data_collector/api_fetch.py

---

## Python Bug Fix Sample

初心者コードのバグ修正サンプルです。

### ■ 内容
- IndexError修正
- Pythonらしいコードへ改善
- 可読性向上

### ■ ファイル
python_bug_fix_sample/fix_example.py

---

## 使用技術

- Python 3
- requests
- BeautifulSoup
- pandas（一部）

---

## 想定案件

・Webスクレイピング案件  
・CSV加工案件  
・APIデータ取得案件  
・Pythonコード修正案件  

クラウドソーシングでの開発案件を想定しています。
