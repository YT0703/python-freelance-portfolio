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
## Auto Scraping Tool（定期実行対応・実務仕様）

Webサイトからデータを定期的に取得し、自動でCSV保存を行う業務自動化ツールです。
実務案件で多い「継続的なデータ収集」を想定して設計しています。

## ■ 実行結果（サンプル）

※以下は出力CSVの一部です

![sukureiping02](https://github.com/user-attachments/assets/9f52dec3-b3bc-4753-aa54-41333618e784)


## ■ 機能

* Webスクレイピング（複数ページ対応）
* CSV自動保存（日時付きファイル）
* ログ出力（logs/app.log）
* 定期実行（バッチ処理）
* エラーハンドリング（処理継続設計）

## ■ 実行方法

### 通常実行

```bash
python main.py
```

### 定期実行（自動化）

```bash
python scheduler.py
```

※ 指定間隔ごとに自動でスクレイピングを実行します

## ■ 出力内容

* 書籍タイトル
* 価格（数値変換済み）
* 在庫状況
* 評価（数値化）
* 商品URL

## ■ 出力ファイル

* output/books_YYYYMMDD_HHMMSS.csv
* logs/app.log

## ■ 技術ポイント

* datetimeによるユニークファイル生成（上書き防止）
* loggingによる実行ログ管理
* time.sleepによる簡易スケジューリング
* 例外処理による安定稼働設計
* 実務を想定したバッチ処理構成

## ■ 想定案件

* 定期的なデータ収集ツール開発
* 価格監視・競合調査ツール
* 情報収集の自動化
* 業務効率化ツール開発

## ■ ファイル構成

auto_scraping_tool/
├── main.py
├── scraper.py
├── utils.py
├── config.py
├── scheduler.py
├── logs/
└── output/

---
## Books Scraping Tool

Books to Scrapeから書籍データを取得し、CSVに保存するツールです。

## ■ 実行結果（サンプル）

※以下は出力CSVの一部です

![sukureipig01](https://github.com/user-attachments/assets/42c4c308-3431-4b82-8f54-241ef31d0423)


### ■ 機能
- ページネーション対応（複数ページ一括取得）
- 書籍データのスクレイピング
- CSV保存
- 重複データ削除
- エラーハンドリング対応
- ログ出力（実行状況の可視化）
- 実行時間計測

## ■ 実行方法

```bash
python main.py
```

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
