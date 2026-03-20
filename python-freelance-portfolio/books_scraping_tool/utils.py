import csv
import os

FIELDS = ["title", "price", "availability", "rating", "link"]

def save_to_csv(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    file_exists = os.path.isfile(filepath)

    with open(filepath, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)

        if not file_exists:
            writer.writeheader()

        for row in data:
            writer.writerow(row)


def remove_duplicates(filepath):
    if not os.path.exists(filepath):
        return

    seen = set()
    unique_rows = []

    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            key = row["link"]
            if key not in seen:
                seen.add(key)
                unique_rows.append(row)

    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(unique_rows)