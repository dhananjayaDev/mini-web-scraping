# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_with_bs4(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='card-body')
    print("🧼 BeautifulSoup Results:")
    for item in items:
        name = item.find('h5').text.strip()
        price = item.find('span', class_='price').text.strip()
        print(f"{name}: ${price}")

def scrape_with_selenium(url):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    print("🕷️ Selenium Results:")
    items = soup.find_all('div', class_='card-body')
    for item in items:
        name = item.find('h5').text.strip()
        price = item.find('span', class_='price').text.strip()
        print(f"{name}: ${price}")

if __name__ == "__main__":
    target_url = "http://localhost:5000"
    scrape_with_bs4(target_url)
    scrape_with_selenium(target_url)
