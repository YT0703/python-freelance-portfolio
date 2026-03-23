"""
project: dynamic_scraping_sample.py

概要：
ログイン後の動的ページを想定し、
「1件の価格データを安定的に取得する」サンプルコード

※ポートフォリオ用のため、特定サイトには依存しない構成
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time


def setup_driver():
    """ブラウザ初期化"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)


def wait_for_page_load(driver):
    """
    動的ページの読み込み完了を待機
    → 「円」が表示されるまで待つ
    """
    wait = WebDriverWait(driver, 30)
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'円')]"))
    )


def extract_price(elements):
    """
    価格抽出ロジック
    ・坪単価などのノイズを除外
    ・5桁以上の価格を優先
    """
    for el in elements:
        text = el.text.strip()

        # ノイズ除外
        if "坪単価" in text:
            continue

        # 賃料パターン（例：150,000円）
        match = re.search(r"\d{2,3},?\d{3}円", text)

        if match:
            return match.group(), el

    return None, None


def main():
    driver = setup_driver()

    # ダミーURL（任意で変更）
    driver.get("https://example.com")

    print("ログインしてください（手動）")
    input("ログイン後 Enter：")

    print("対象ページを開いてください")
    input("開いたら Enter：")

    # ページロード待機
    wait_for_page_load(driver)
    print("ページ読み込み完了")

    # 要素取得
    elements = driver.find_elements(By.XPATH, "//*[contains(text(),'円')]")
    print("候補数:", len(elements))

    # 価格抽出
    price, element = extract_price(elements)

    if price:
        print("✅ 取得成功:", price)

        # 親要素から全体情報取得
        parent = element.find_element(
            By.XPATH, "./ancestor::*[self::tr or self::div][1]"
        )

        print("===== データ =====")
        print(parent.text)

    else:
        print("❌ 価格取得失敗")


if __name__ == "__main__":
    main()