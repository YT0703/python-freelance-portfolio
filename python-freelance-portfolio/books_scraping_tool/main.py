import logging
import time
import os
os.makedirs("output", exist_ok=True)
from scraper import fetch_books
from utils import save_to_csv, remove_duplicates
from config import BASE_URL, START_PAGE, END_PAGE, OUTPUT_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    start_time = time.time()

    all_books = []

    for page in range(START_PAGE, END_PAGE + 1):
        url = BASE_URL.format(page)
        logging.info(f"取得中: {url}")

        books = fetch_books(url)

        if books:
            logging.info(f"{len(books)}件取得")
            all_books.extend(books)
        else:
            logging.warning("データ取得失敗 or 0件")

    if not all_books:
        logging.error("データ取得失敗")
        return

    # 重複削除
    all_books = remove_duplicates(all_books)
    
    # その後CSV保存
    save_to_csv(all_books, OUTPUT_FILE)

    logging.info("CSV保存完了")

    end_time = time.time()
    logging.info(f"実行時間: {end_time - start_time:.2f}秒")


if __name__ == "__main__":
    main()