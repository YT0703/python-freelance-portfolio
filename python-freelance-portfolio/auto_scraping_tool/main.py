import logging
import time
import os
os.makedirs("logs", exist_ok=True)
from scraper import fetch_books
from utils import create_output_path, save_to_csv
from config import BASE_URL, START_PAGE, END_PAGE, OUTPUT_DIR, LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    start = time.time()

    all_books = []

    for page in range(START_PAGE, END_PAGE + 1):
        url = BASE_URL.format(page)
        logging.info(f"取得中: {url}")

        try:
            books = fetch_books(url)
            logging.info(f"{len(books)}件取得")
            all_books.extend(books)
        except Exception as e:
            logging.error(f"エラー: {e}")

    if not all_books:
        logging.warning("データなし")
        return

    output_path = create_output_path(OUTPUT_DIR)
    save_to_csv(all_books, output_path)

    logging.info(f"保存完了: {output_path}")

    end = time.time()
    logging.info(f"実行時間: {end - start:.2f}秒")


if __name__ == "__main__":
    run()