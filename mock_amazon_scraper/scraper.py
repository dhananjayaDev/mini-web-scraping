from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

def scrape_mock_amazon(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='card-body')

    scraped_products = []
    for item in items:
        name = item.find('h5').text.strip()
        price = item.find('span', class_='price').text.strip()
        image_tag = item.find_previous_sibling('img')
        image = image_tag['src'] if image_tag else ''
        rating = item.find('p', class_='rating')
        delivery = item.find('p', class_='delivery')

        scraped_products.append({
            "name": name,
            "price": float(price),
            "image": image,
            "rating": rating.text.strip() if rating else "N/A",
            "delivery": delivery.text.strip() if delivery else "N/A"
        })

    # Optional: Save to JSON
    with open("scraped_data.json", "w") as f:
        json.dump(scraped_products, f, indent=2)

    return scraped_products

@app.route("/")
def show_scraped():
    products = scrape_mock_amazon("http://localhost:5000")
    return render_template("scraper.html", products=products)

if __name__ == "__main__":
    app.run(port=5001, debug=True)