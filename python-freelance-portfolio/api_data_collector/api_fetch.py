import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_api_data():
    response = requests.get(API_URL)
    data = response.json()
    return data


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["userId", "id", "title"])

        for item in data:
            writer.writerow([
                item["userId"],
                item["id"],
                item["title"]
            ])

    print("Saved API data to", filename)


if __name__ == "__main__":
    data = fetch_api_data()
    save_to_csv(data, "api_data.csv")