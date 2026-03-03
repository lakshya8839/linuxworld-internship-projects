from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# --- CONFIG ---
tweet_url = "https://twitter.com/elonmusk/status/1933399839490126217"
chrome_user = "lakshya"  # <-- change only if your username is different

# --- Setup Chrome options (non-headless, safe mode) ---
options = Options()
options.add_argument(f"user-data-dir=C:/Users/{chrome_user}/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Default")  # Change if you use a different profile

# ✅ Stability flags to avoid crash
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

# Optional: Remove logging
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# --- Launch Chrome ---
print("🚀 Launching Chrome using your profile...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    print("🔗 Opening tweet...")
    driver.get(tweet_url)
    time.sleep(5)

    print("📜 Scrolling to load replies...")
    for i in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(3, 5))

    print("🔍 Extracting replies...")
    articles = driver.find_elements(By.XPATH, "//article")
    print(f"Found {len(articles)} tweet blocks (original + replies)")

    replies = []
    for article in articles[1:]:  # Skip the main tweet
        try:
            text = article.text.strip()
            if text and text not in replies:
                replies.append(text)
        except:
            continue

    # --- Save replies ---
    with open("replies.txt", "w", encoding="utf-8") as f:
        for reply in replies:
            f.write(reply + "\n\n")

    with open("page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    if replies:
        print(f"\n✅ {len(replies)} replies saved to replies.txt")
    else:
        print("❌ No replies found. Try increasing scrolls or checking login status.")

finally:
    driver.quit()
