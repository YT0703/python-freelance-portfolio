import time
from main import run
from config import INTERVAL_MINUTES

def start():
    while True:
        print("実行開始")
        run()
        print(f"{INTERVAL_MINUTES}分待機")
        time.sleep(INTERVAL_MINUTES * 60)

if __name__ == "__main__":
    start()