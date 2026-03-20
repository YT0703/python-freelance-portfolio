import csv
import os
from datetime import datetime

FIELDS = ["title", "price", "availability", "rating", "link"]

def create_output_path(base_dir):
    os.makedirs(base_dir, exist_ok=True)

    # 秒まで含めてユニーク化
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    return os.path.join(base_dir, f"books_{date_str}.csv")


def save_to_csv(data, filepath):
    try:
        with open(filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

            for row in data:
                writer.writerow(row)

    except PermissionError:
        print("CSVファイルが開かれています。閉じて再実行してください。")

    except Exception as e:
        print(f"CSV保存エラー: {e}")
def remove_duplicates(data):
    seen = set()
    unique_data = []

    for item in data:
        key = (item["title"], item["price"]) # タイトルで重複判定

        if key not in seen:
            seen.add(key)
            unique_data.append(item)

    return unique_data