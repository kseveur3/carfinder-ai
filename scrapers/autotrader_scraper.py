# Sample scraper setup using Playwright
from playwright.sync_api import sync_playwright

def scrape_autotrader():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.autotrader.com/cars-for-sale")
        print(page.title())
        browser.close()
