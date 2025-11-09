import sys
import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

DEFAULT_URL = "https://www.basketball-reference.com/players/d/duranke01.html"

def create_driver(headless: bool = True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1200,800")
    opts.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)

def main():
    url = sys.argv[1].strip() if len(sys.argv) > 1 else DEFAULT_URL
    print("Using URL:", url)

    # Inline extraction of player tag (replaces the removed get_player_tag function)
    m = re.search(r"/players/[a-z]/([^/]+)\.html", url or "")
    player = m.group(1) if m else "player"

    driver = create_driver(headless=True)
    try:
        driver.get(url)
        time.sleep(2)  
        html = driver.page_source
    finally:
        driver.quit()

    try:
        tables = pd.read_html(html, flavor="lxml")
    except Exception as e:
        print("Error parsing tables:", e)
        return

    per_game = None
    for df in tables:
        cols = [str(c).strip() for c in df.columns]
        if "Season" in cols and "PTS" in cols:
            per_game = df
            break

    if per_game is None:
        print("Couldn't find per_game table.")
        return

    out = f"{player}_per_game.csv"
    per_game.to_csv(out, index=False)
    print("Saved:", out)

if __name__ == "__main__":
    main()
