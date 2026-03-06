import csv
from collections import defaultdict

def summarize_csv(input_file, output_file):
    summary = defaultdict(int)

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            category = row["category"]
            amount = int(row["amount"])
            summary[category] += amount

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "total"])

        for category, total in summary.items():
            writer.writerow([category, total])

    print("CSV summary created:", output_file)


if __name__ == "__main__":
    summarize_csv("sample.csv", "summary.csv")